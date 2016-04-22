For system administrators
=========================

.. _configure-repository-location:

Configure the repository location
---------------------------------

The |connect_plugin| can work with the standard remote *Boundless QGIS Plugin Repository*, use an internal repository (e.g. in Docker container) or install plugins from a local folder (useful for customers with special requirements, when connection to external resources is not possible).

On its first run, the |connect_plugin| will look for ``$HOME/.qgis2/repoUrl.txt`` file. If the file exists, the plugin will read the repository URL/path from it and use this as a location for the plugins repository. Otherwise, if the file is not found, the standard Boundless QGIS Plugins Repository URL will be used. After this, the file will be deleted.

.. warning::

   Creating a new file after the first launch of |connect_plugin| will have no effect whatsoever. The plugin will ignore the new file and will continue to use the already saved repository location.

The ``$HOME/.qgis2/repoUrl.txt`` file is an INI-like text file with single ``general`` section and only one key-value pair, for example:

::

  [general]
  repoUrl=http://qgis.boundlessgeo.com/plugins/plugins.xml

The value of the ``repoUrl`` key with repository location can be:

* A **Repository URL**. The plugin will add this URL to the list of available plugins repositories and QGIS *Plugin Manager* can be used to access it. This is the default.
* An **absolute path to the plugins directory**. In this case, the directory should contain plugins packages as well as repository description file ``plugins.xml``. With this option, nothing is added to the QGIS settings, as QGIS
  *Plugin Manager* can not handle directories yet.

.. TODO:: Make an example of an XML

.. _add-additional-plugins:

Installing additional plugins by default
----------------------------------------

If the system administrator wants to automatically install a bundle of additional plugins during the post-installation step, he can create a directory `.qgis2/first-run-plugins` under the user folder and put all the desired plugins ZIP packages in it.

The *First Run wizard* tool from |connect_plugin| will check if the directory exists and will install all the ZIP packages from it. Notice that the packages will be removed after hte installation.
