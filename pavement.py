import os
from paver.easy import *
# this pulls in the sphinx target
from paver.doctools import html
import shutil
import requests

def pluginNames():
    url = "https://api.github.com/orgs/boundlessgeo/repos"
    r = requests.get(url)
    r.raise_for_status()
    repos = r.json()    
    names = [repo["name"] for repo in repos  if  repo["name"].startswith("qgis-") and repo["name"].endswith("-plugin")]
    while True:
        links = r.headers["link"].split(",")
        if "next" not in links[0]:
            break
        next = links[0].split(";")[0][1:-1]        
        r = requests.get(next)
        r.raise_for_status()
        repos = r.json()    
        names.extend([repo["name"] for repo in repos  if  repo["name"].startswith("qgis-") and repo["name"].endswith("-plugin")])

    # Add private repos
    private_repos = ['qgis-imagediscovery-plugin',
                     'qgis-terrainanalysis-plugin',
                     'qgis-navigation-plugin',
                     'qgis-master-pass-cxxplugin'
                     ]
    names += private_repos
    return names

@task
@cmdopts([
    ('stable', 's', 'build docs for latest stable version')
])
def all(options):
    fetch()
    builddocs(options)
    deploy()
@task

def fetch(options):
    '''clone all plugin repos'''
    plugins = pluginNames()
    cwd = os.getcwd()
    tmpDir = os.path.join(cwd, 'tmp')
    if not os.path.exists(tmpDir):
        os.mkdir(tmpDir)
    for plugin in plugins:
        print "\nFetching %s" % plugin
        repoPath = os.path.join(tmpDir, plugin)
        if os.path.exists(repoPath):            
            os.chdir(repoPath)
            sh("git pull")
            sh("git submodule update --init --remote")
        else:
            sh("git clone --recursive https://github.com/boundlessgeo/%s.git %s" % (plugin, repoPath))
    os.chdir(cwd)

@task
@cmdopts([
    ('stable', 's', 'build docs for latest stable version'),
    ('released', 'r', 'build docs for the released version'),
])
def builddocs():
    '''create html docs from sphinx files'''     
    pluginsIndex = []
    cwd = os.getcwd()
    tmpDir = os.path.join(cwd, 'tmp')
    subfolders = [os.path.join(tmpDir, name) for name in os.listdir(tmpDir)
            if os.path.isdir(os.path.join(tmpDir, name))]
    for folder in subfolders:
        docFolder = os.path.join(folder, 'docs')
        if os.path.exists(docFolder):
            os.chdir(folder)
            helpFile = os.path.join(folder, "README.rst")
            if not os.path.exists(helpFile):
                helpFile = os.path.join(folder, "README.md")
            with open(helpFile) as f:
                title = None
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("#"):
                        title = line.split("#")[-1]
                        break
                    elif "===" in line:
                        title = lines[i - 1]
                        break
                if title is None:
                    title = os.path.basename(folder).split("-")[1]
                pluginsIndex.append((os.path.basename(folder).split("-")[1], title))
            if getattr(options, 'stable', False):
                try:
                    tag = sh("git describe --abbrev=0 --tags", capture=True)
                except:
                    continue # in case no tags exist yet
                sh("git checkout %s" % tag)
            if getattr(options, 'released', False):
                buildFolder = os.path.join(docFolder, 'build')
                if os.path.exists(buildFolder):
                    shutil.rmtree(buildFolder)
                try:
                    sh("git ls-remote --exit-code --heads origin "
                       "release_docs", capture=True)
                    sh("git checkout release_docs")
                except:
                    continue # in case no release_docs exist yet

            print ("\nBuilding %s") % title
            if getattr(options, 'stable', False) or getattr(options, 'released', False):
                sh("paver builddocs -c -s boundless_product")
                sh("git checkout master")
            else:
                sh("paver builddocs -c")
    
    os.chdir(cwd)
    '''build index'''

    with open("index_template.html") as f:
        s = f.read()
    pluginsIndex.sort()
    indexItems = "\n".join(["<li><a href='%s/index.html'>%s</a></li>" % (a[0], a[1]) for a in pluginsIndex])    
    s = s.replace("[PLUGINS]", indexItems)
    with open("tmp/index.html", "w") as f:
        f.write(s)

@task    
def deploy():
    sh("git checkout gh-pages")
    cwd = os.getcwd()
    tmpDir = os.path.join(cwd, 'tmp')
    subfolders = [name for name in os.listdir(tmpDir)
            if os.path.isdir(os.path.join(tmpDir, name))]
    for folder in subfolders:
        print "\nDeploying %s ..." % folder
        src = os.path.join(tmpDir, folder, 'docs', 'build', 'html')
        if os.path.exists(src):
            dst = os.path.join(cwd,  folder.split("-")[1])
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
    shutil.copyfile(os.path.join(tmpDir, "index.html"), os.path.join(cwd, "index.html"))
    sh('git add .')
    sh('git commit -m "docs update"')
    sh("git push origin gh-pages")
    sh("git checkout master")

@task
def deployoffline():
    cwd = os.getcwd()
    tmpDir = os.path.join(cwd, 'tmp')
    subfolders = [name for name in os.listdir(tmpDir)
            if os.path.isdir(os.path.join(tmpDir, name))]
    for folder in subfolders:
        print "\nDeploying %s ..." % folder
        src = os.path.join(tmpDir, folder, 'docs', 'build', 'html')
        if os.path.exists(src):
            dst = os.path.join(cwd, 'output',  folder.split("-")[1])
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
    shutil.copyfile(os.path.join(tmpDir, 'index.html'), os.path.join(cwd, 'output', "index.html"))
    staticDir = os.path.join(cwd, 'output', '_static')
    if os.path.exists(staticDir):
        shutil.rmtree(staticDir)
    shutil.copytree(os.path.join(cwd, '_static'), staticDir)
