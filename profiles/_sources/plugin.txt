QGIS Profiles plugin
=====================

The QGIS profiles plugin allows to quickly set up your QGIS environment according a predefined configuration.

Configurations are supplied with the plugin itself, and can also be created at runtime, to store the current state of your QGIS instance.

A configuration includes settings for the following elements:

- Visible panels

- Visible menus and their names

- Visible buttons and their placement in the toolbar

- Active plugins. If a plugin is not installed, the Profiles Plugin will install it and activate it.



Setting a profile
-----------------

All available profiles are displayed in the *Settings/Profiles* menu group. Menu entries are grouped themselves according to categories.

To set a profile, click on the corresponding menu item. The interface will be adapted according the the profile settings.

If it is the first time that you use the Profiles Plugin, you will see a message like the following one:

.. figure:: warning.png
   :align: center

In order to allow you recovering your current configuration, the state of our QGIS interface is saved as a profile itself. This won't happen again once it has been stored, unless you delete all available recovery profiles (you can create more, as we will see next). Profiles containing previous system configurations will not be shown in the *Settings* menus, and to access them you should use the profiles manager.

When applying a profile, the Profiles plugin will try to optimally arrange the visible toolbars. If you later modify the arrangement manually by dragging toolbars, the new configuration will be stored, and applied each time the profile is applied again.

The profiles manager
---------------------

To open the profile manager, click on the *Plugin/Profiles/Profiles manager...* menu.


.. figure:: manager.png
   :align: center

The profiles manager contains a list of all available plugins. It shows them organized in groups, as they are shown in the *Settings/Profiles* menu. An additional group with custom profiles is shown at the bottom of the profiles tree.

Custom profiles are created, as we have seen, the first time you set up a profile, to create a restoration point. They can also be created manually at anytime, by clicking on the "Store current configuration as profile" button. A new profile entry will be added to the group of custom profiles.

Clicking on any profile will display information about it, such as a description. A link to set that profile is available along with the description, so you can set it without having to go the the *Settings/Profiles* menu.

For custom profiles, a link to delete the profile is also shown. Built-in profiles cannot be deleted.

Automatically set a profile on startup
---------------------------------------

Some of the changes introduced by a profile are not permanent, such as the menu configurations. When you reopen QGIS, your interface will not be configured in the same way as after you applied a profile for the last time. You have to apply that profile again.

If you want to have a profile applied automatically when you start QGIS, select the *Plugins/Profiles/Auto-load last profile on QGIS start*. The last applied profile will be reapplied when you open QGIS.

If plugins required by the profile have been uninstalled and the Profile Plugin has to reinstall them, the profile will not be applied.

To disable this functionality and not make any modification to the QGIS interface upon startup, unselect the menu item by clicking again on it.

