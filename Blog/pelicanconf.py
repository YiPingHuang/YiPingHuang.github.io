#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yi-Ping Huang'
SITENAME = u'Some kind of notepad for myself...'
SITEURL = ''

THEME='gum'

TIMEZONE = 'USA/Boulder'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Plugins
PLUGIN_PATH='/home/yi-ping/virtualenvs/pelican/pelican-plugins'
PLUGINS =['render_math','liquid_tags.img', 'liquid_tags.video', 'liquid_tags.youtube', 'liquid_tags.vimeo','liquid_tags.include_code', 'liquid_tags.notebook']

# For ipython
EXTRA_HEADER=open('_nb_header.html').read().decode('utf-8')