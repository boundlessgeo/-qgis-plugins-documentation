Addining Boundless Connect to installer
=======================================

Plugin can be placed in the QGIS python plugins directory, where all "core"
plugins stored, before creating installer. Alternatively it can be extracted
and placed in the correct place, e.g. QGIS plugins directory or users plugins
directory, by installer during installation.

Boundless Connect should be enabled by default in our QGIS build, e.g. via
adding corresponding entry to the Windows registry at the install stage. This
can be done with the following NSIS code
::

  WriteRegStr HKEY_CURRENT_USER "Software\QGIS\QGIS2\Plugins" "boundlessconnect" "true"


Configuration
-------------

There is only one thing to configure now --- repository location. Plugin can
work with standard Boundless Plugins Repository, use internal repository (e.g.
in Docker container) or install plugins from local folder (useful for customers
with special requirements, when connection to external resources is not
possible).

On first run *Boundless Connect* looks for ``$HOME/.qgis2/repoUrl.txt`` file.
If this file exists, plugin will read repository URL from it and use this URL
as location of plugins repository. Otherwise standard Boundless Plugins
Repository will be used. After reading repository URL file will be deleted.
Creating new file after first launch of *Boundless Connect* will make no
effect, it will ignore new file and continue to use already saved repository
address.

The ``$HOME/.qgis2/repoUrl.txt`` file is an INI-like text file with single
``general`` section and only one key-value pair, for example
::

  [general]
  repoUrl=http://qgis.boundlessgeo.com/plugins/plugins.xml


Repository location (value of the ``repoUrl`` key) can be:

* repository URL. Plugin will add this URL to the list of available plugins
  repositories, so QGIS *Plugin Manager* can be used to access it. This is
  default.
* absolute path to the plugins directory. In such case this directory should
  contain plugins packages as well as repository description file
  ``plugins.xml``. In this case nothing added to the QGIS settings, as QGIS
  *Plugin Manager* can not handle directories yet.

When QGIS starts and Boundless repository location is an URL, Connect plugin
will add Boundless Plugins Repository to the *Plugin Manager*'s list of
available plugin repositories. NOTE: only repository URL added, user should
specify his credentials with *First Run* wizard or using *Plugin Manager*.

If repository locations is a path, nothing added to *Plugin Manager*. User
should use *Plugins → Boundless Connect → Manage plugins (local folder)* to
install plugins from local directory-based repository.

Installing plugins from "standard" location
===========================================

If sysadmin wants to install some additional plugins at the post-installation
step, it is necessary to create directory `~/.qgis2/first-run-plugins` and put
plugins ZIP packages in it.

*First Run* wizard from Boundless Connect will check if this directory exists
and install all packages from it.

NOTE: in current implementation this happens on every run of the wizard.
