Usage
=====

When QGIS is started for the first time with the |connect_plugin| (it's activated by default in |BLQGIS|) it checks if there are Boundless plugins installed or not. Then, depending on the result of this check, one of the following scenarios will be activated:

* If no **Boundless plugins are found or only some of them are installed**, |connect_plugin| will start *First Run wizard* to help the user setting up *Boundless QGIS Plugins Repository* and install additional plugins. See :ref:`first-run-wizard` section for more details.
* If **all Boundless plugins are found, but some of them are outdated**, the |connect_plugin| will propose to update the plugins automatically. See :ref:`updating-plugins` section for more details.
* If **all Boundless plugins are found and they are the latest version**, the user will be notified that no additional actions are required.

After any of the scenarios above, the user can always review and manage installed plugins either by using the *Plugin manager* or by re-running the *First Run Wizard* tool. Please see :ref:`managing-plugins` for details.

.. _first-run-wizard:

First Run wizard
----------------

The aim of the *First Run wizard* is to help the user to setup the `Boundless QGIS Plugin Repository <http://qgis.boundlessgeo.com>`_ and install additional plugins, both Boundless and 3rd party ones (depending on what have been configured by the system administrator).

The wizard will run automatically when QGIS is started for the first time with the |connect_plugin| activated or whenever this plugin is updated. 

If at the time, you don't want to go through the wizard, you can safely close it. While
the wizard starts automatically only once, you can open it at any time from the :menuselection:`Plugins --> Boundless Connect --> First Run wizard` menu item.

The first wizard's dialog contains general information about it and what it will do. If you have installed any unsupported Boundless plugins (deprecated plugins that were replaced by others, e.g., OpenGeo Explorer was replaced by GeoServer Explorer) these plugins will be listed at the welcome page suggesting you to remove them.

.. figure:: img/welcome-page.png
   :align: center
   
   First Run Wizard welcome dialog

Please read the information on this dialog and press :guilabel:`Next` button to go to the next step.

At this step, *First Run wizard* will behave differently depending on the
|connect_plugin| configuration.

If your organization works with the remote *Boundless QGIS Plugin Repository*, the wizard will ask you to enter the credentials to access the repository. Press the :guilabel:`add` button in the *Boundless credentials* dialog, as shown below.

.. figure:: img/credentials-page.png
   :align: center

   Boundless credentials dialog

.. note:: 

   If you haven't done this before, QGIS will ask you to set a master password. This password will be used to store all your credentials inside QGIS, e.g., username and password  for connecting spatial databases. Choose the password wiselly and make sure you memorize it, as **the password is not retrivable**. Press :guilabel:`Save` to go to the next dialog.
   
   .. figure:: img/add-master-password.png
      :align: center

   Setting QGIS master authentication password

In the next dialog, enter the provided Boundless credentials as shown below, and press :guilabel:`Save` to store the credentials in QGIS authentication database.

.. figure:: img/enter-credentials.png
   :align: center

   Boundless credentials dialog

If the |connect_plugin| was configured to use a local directory-based repository, all the authentication steps will be skipped.

In the next dialog, the user has three options:

* :guilabel:`Install all available plugins automatically`, will silently install and/or update all Boundless plugins (both from the QGIS Official Plugins Repository or the ones available to him in the Boundless QGIS Plugins Repository).
* :guilabel:`Open Plugin Manager (all plugins)`, will open the plugin manager, where the user can manually choose which plugins to install (includes all plugins available in both repositories).
* :guilabel:`Open Plugin Manager (Boundless plugins only)` will open the plugin manager as well, but showing only Boundless plugins available, making it easier to find.

.. figure:: img/plugins-page.png
   :align: center
   
   Plugin installation dialog

.. note::

   Deprecated Boundless plugins will not be installed automatically. But, if you already have such plugins installed and there are new versions available, they will be updated.

After this, if previously configured by the system administrator, |connect_plugin| will install additional plugins (see :ref:`add-additional-plugins` section for more details about it).

.. _updating-plugins:

Updating plugins
----------------

If during the first run of |connect_plugin| (or after its update) is found that all Boundless plugins are already installed, but some of them are outdated, it will propose you to update those plugins automatically.

.. figure:: img/ask-update.png
   :align: center
   
   First Run wizard suggesting to automatically update all plugins.

If you press the :guilabel:`Yes` button, all installed Boundless plugins will be updated automatically. If instead you chose to press the :guilabel:`No` button, pressed nothing else will happen. Notice that you can always update the plugins manually using the *Plugin Manager* (see :ref:'managing-plugins' for more details).

Plugins installation
--------------------

Using |connect_plugin|, plugin installation can be performed in several different ways:

* :ref:`from-remote-repository`
* :ref:`from-local-repository` (through |connect_plugin| only)
* :ref:`from-zip-package` (through |connect_plugin| only)

.. _from-remote-repository:

From a remote plugin repository
...............................

This is the most common way to install plugins, whether from QGIS Official Plugins Repository, Boundless QGIS Plugins Repository or any other remote repository that you may have configured, using the *Plugin manager* directly or through the *First Run wizard* tool.

.. note::
   
   If your organization works with the remote *Boundless QGIS Plugin Repository* it will be necessary to provide credentials to fully access the repository. This can be done using the :ref:`first-run-wizard` as described above or setting them manually using the QGIS *Plugin Manager* settings.

.. _from-local-repository:

From a local repository
.......................

Using |connect_plugin| it's possible to use a local path or network path as a repository (see :ref:`configure-repository-location` section for details on how to set a local repository). If any repository was set that way, the |connect_plugin| will add an additional menu item in :menuselection:`Plugins --> Boundless Connect` named :guilabel:`Manage plugins (local folder)`. This tool should be used when the user wants to install plugins from a local (directory-based) repository. The usage is similar to the *plugin manager*

To active, deactivate or uninstall plugins from a local repository, either the *Plugin Manager* or the *Manage plugins (local folder)* tool can be used.

.. Note::
   
   Since the QGIS *Plugin Manager* does not support directory-based repositories yet, when you uninstall a plugin, previously installed from Boundless local directory-based repository, the following warning will be shown.

   .. figure:: img/plugin-uninstall.png
      :align: center

   This warning can be safely ignored, as you can install or uninstalled the plugin again using :menuselection:`Plugins --> Boundless Connect --> Manage plugins (local folder)` menu item.

.. _from-zip-package:

From a plugin ZIP package
.........................

If you have a plugin package (e.g. previously downloaded from any repository or GitHub)
you can easily install it using the |connect_plugin|, without the need to unpackage it. Go to :menuselection:`Plugins --> Boundless Connect --> Installing plugin from ZIP`, browse to the directory with plugin zip package and select the corresponding file. If the zip file is a valid QGIS plugin package it will be installed and activated.

To deactivate or remove plugins installed whis way, like before, one can use QGIS *Plugin
Manager* from :menuselection:`Plugins --> Manage and Install Plugins...` menu item.

.. _managing-plugins:

Managing plugins
----------------

All plugins added by |connect_plugin| can be deactivated, uninstalled or updated using QGIS *Plugin Manager*. You can access it via the :menuselection:`Plugins --> Manage and Install Plugins...` menu item or, for more selective options, re-running the :ref:`first-run-wizard` tool.

.. figure:: img/managing-plugins.png
   :align: center

   Plugin manager
