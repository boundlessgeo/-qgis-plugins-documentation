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
        repoPath = os.path.join(tmpDir, plugin)
        if os.path.exists(repoPath):            
            os.chdir(repoPath)
            sh("git pull")
        else:
            sh("git clone https://github.com/boundlessgeo/%s.git %s" % (plugin, repoPath))
    os.chdir(cwd)

@task
@cmdopts([
    ('stable', 's', 'build docs for latest stable version')
])
def builddocs():
    '''create html docs from sphinx files'''
    cwd = os.getcwd()
    tmpDir = os.path.join(cwd, 'tmp')
    subfolders = [os.path.join(tmpDir, name) for name in os.listdir(tmpDir)
            if os.path.isdir(os.path.join(tmpDir, name))]
    for folder in subfolders:
        docFolder = os.path.join(folder, 'docs')
        if os.path.exists(docFolder):
            os.chdir(docFolder)
            if getattr(options, 'stable', False):
                try:
                    tag = sh("git describe --abbrev=0 --tags", capture=True)
                except:
                    continue # in case no tags exist yet
                sh("git checkout %s" % tag)
            sh("make html")
            if getattr(options, 'stable', False):
                sh("git checkout master")
    os.chdir(cwd)

@task    
def deploy():
    sh("git checkout gh-pages")
    cwd = os.getcwd()
    tmpDir = os.path.join(cwd, 'tmp')
    subfolders = [name for name in os.listdir(tmpDir)
            if os.path.isdir(os.path.join(tmpDir, name))]
    for folder in subfolders:
        src = os.path.join(tmpDir, folder, 'docs', 'build', 'html')
        dst = os.path.join(cwd,  folder.split("-")[1])
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
    sh("git commit -m 'docs update'")
    sh("git push origin gh-pages")
    sh("git checkout master")

