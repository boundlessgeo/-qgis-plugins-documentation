QGIS Documentation
##################

Tools to organize documentation for Boundless QGIS plugins

Currently there is just a simple paver file w ith tasks that fetch, build and deploy documentation.

To create and deploy html docs corresponding to the latest version of each plugin (the current master branch), run

::

    paver all

If you want to create documentation of the latest stable version of each plugin, run

::

    paver all --stable