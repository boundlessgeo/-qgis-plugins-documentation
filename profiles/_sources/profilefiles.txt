Profile files
--------------

A profile file contain all the elements needed to configure the QGIS interface according to a profile.

It's stored as a JSON file, with the following elements:

- panels: The names of panels to show, with their QT object names. These panels will be made visible. All other panels not listed here will be hidden. If not present, panels from the default profile will be set.

- menus: Dictionaries of menus to display. Menus are referred with their full path (including names of all parent menus) used as keys of the dict. Values are the name of the menu entry, to allow renaming of the menu item. If not present, menus from the default profile will be set.


- buttons: Dictionaries of toolbars. Each dictionary represents a toolbar from the available ones, with the list of buttons to include, referenced using their QT object name. If a button is not added, it wont be shown. IF the value associated to the key representing a button is null, the button is shown in its original toolbar. Otherwise, a new toolbar with the name used as value will be created. This allows to create new toolbars and group buttons in a different way. If the 'buttons' property is not present, buttons from the default profile will be set. If it's an empty dictionary, all buttons from the toolbar will be added.

Notice that, if a button is not shown, the corresponding menu item might not be visible if both the button and the menu use the same action object.


- plugins: names of plugins to activate. If a plugin is not installed, installation should be proposed to the user when changing. If plugins to activate add menu entries to the menu bar, those menu entries should be added to the *menus* list, otherwise they wont be shown. This is configured like this to allow having a plugin enabled, but only have certain menus from it available, or even no menus at all (so the plugin is only available for other plugins or to be used programatically)


For each json file in the ``userprofiles`` folder, a Profile object is created and registered, and a menu entry corresponding to that profile will be added to the *Profiles* menu. If your profile requires more than what the json file allows to configure, you can add a python file with code to be run when applying the profile.

To do that, just add a python file with the same name as the json file that contains the profile description, and add a function called ``apply`` to it. That function will be run when the profile is applied.

Profiles files (both json and python files) must be saved into the ``userprofiles`` folder, in order to be used by the profiles plugin.

Instead of writing profiles manually, helper methods can be used to write them based on the current QGIS configuration. First, customize your QGIS UI using the built-in functionality. Then run the following code

::

	from profiles.utils import *
	saveCurrentStatus("path/to/file/to/create/", "MyProfileName")

An additional parameter with an array of constants can be passed to indicate what will be saved in the profile. Available constants are *PLUGINS, MENUS, BUTTONS* and *PANELS*.

For instance, for creating a profile that only stores menus and buttons, the following can be executed:

::

	from profiles.utils import *
	saveCurrentStatus("path/to/file/to/create/", "MyProfileName", [MENUS, BUTTONS])

If this parameter is not passed, all elements will be stored in the profile definition.