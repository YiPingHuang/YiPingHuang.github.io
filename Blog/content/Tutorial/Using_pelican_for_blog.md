Title: Using pelican for Blog
Slug: Using-Pelican-Ubuntu 14.04
Date: 2014/05/29
Tags: Pelican, Ubuntu, Tutorial
Summary: Generate static blog posts by pelican

Using pelican to generate blog posts is quite convenient. After several steps,
your blog is ready to go. To do that, we need to learn two tools at least:

1. How to use markdown.
2. Basic pelican operation.

Following are some useful links

Link:http://hackercodex.com/guide/pelican-static-site-generator-install/

* First, using pelican-quickstart to generate the structure.
* Second, install your favorite theme by
pelican-themes --install $PATH_TO_THEME --verbose
* Third, set the variable THEME= favorite theme in pelicanconf.py.

In order to activate $Latex$ display, we need to activate the plugin
'render_math'.

* Get the plugin.
* Set the plugin path by
PLUGIN_PATH='path to pelican-plugins'
* Activate the plugins related to $Latex$ display
PLUGINS=['render_math']

For the notebook of ipython, we need the plugin
{% notebook XKCD_Plot.ipynb %}
