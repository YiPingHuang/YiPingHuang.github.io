#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yi-Ping Huang'
SITENAME = u'Some kind of notepad for myself...details about coding/physics/linux'
SITEURL = ''

THEME='pelican-simplegrey'
# for pure
# COVER_IMG_URL='Hualien.jpg'
# PROFILE_IMAGE_URL='Hualien.jpg'
# TAGLINE=True
# DISQUS_SITENAME=True
# GOOGLE_ANALYTICS=True

TIMEZONE = 'USA/Boulder'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Homepage','https://yipinghuang.github.io/'),
          ('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          )

# Social widget
SOCIAL = (('Github', 'https://github.com/YiPingHuang'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Plugins
PLUGIN_PATH='/home/yi-ping/virtualenvs/pelican/pelican-plugins'
PLUGINS =['render_math','liquid_tags.img', 'liquid_tags.video', 'liquid_tags.youtube', 'liquid_tags.vimeo','liquid_tags.include_code', 'liquid_tags.notebook']

# For ipython
EXTRA_HEADER=open('_nb_header.html').read().decode('utf-8')
