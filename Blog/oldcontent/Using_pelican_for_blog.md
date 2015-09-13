Title: Using pelican for Blog
Slug: Using-Pelican-Ubuntu-14.04
Date: 2014/05/29
Tags: Pelican, Ubuntu-14.04, Tutorial
Summary: Generating static blog posts by pelican is convenient. This post describes the necessary information to set up pelican such that it supports $LaTeX$ and ipython presentation.

Using pelican to generate static blog posts is quite convenient. I create this
blog as a notepad to record some technical details about how to set things up
for those things I would like to learn.

I would like my blog to support several features:

* Easy to write posts.
* Support $\LaTeX$, so I can type some formula when I need to.
* Some nice presentation about codes.

Some years ago, I feel it is impossible to achieve the three criteria
simultaneously. Luckily, thanks to
the community of pelican and other groups of people to glue those three features
together. Now, pelican provides an elegant framework for people like me to setup a blog.

To do that, we need to learn several tools at least:

* How to use markdown: There is a tutorial claiming you can learn [markdow](http://markdowntutorial.com/) in 10 minutes, which is quite true for my need.
* Basic pelican operation:
	* Following are some useful
[links](http://hackercodex.com/guide/pelican-static-site-generator-install) to
setup the system.
	* Find some details about pelican form the official documentation.

Now I will break down those steps into pieces.

* First, using pelican-quickstart to generate the structure.
* Second, install your favorite theme by

	pelican-themes --install $PATH_TO_THEME --verbose

* Third, set the variable THEME= FAVORITE_THEME in pelicanconf.py.

In order to activate $\LaTeX$ display, we need to activate the plugin
'render_math'.

* Get the plugin from git.
* Set following parameters in pelicanconf.py
	* Set the plugin path by

	PLUGIN_PATH='PATH_TO_PELICAN-PLUGINS'

	* Activate the plugins related to $\LaTeX$ display

	PLUGINS=['render_math']

For the notebook of ipython, we need the plugin [Liquid-style
Tags](https://github.com/getpelican/pelican-plugins/blob/master/liquid_tags).

* Following the instruction to install and activate the plugin. 

	
* Create a sub folder under contnet named notebooks. And put the ipython files
you want to included in the post there.
* Insert the liquid tags in the post's markdown file: 
* In pelicanconf.py, include the line

	EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

* I don't actually know where to add following lines... but I am happy with the
presentation.

	\{% if EXTRA_HEADER %\}
	\{\{ EXTRA_HEADER \}\}
	\{% endif %\}

## Here is the content of the including ipython file.

{% notebook XKCD_Plot.ipynb %}
