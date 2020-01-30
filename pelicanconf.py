#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ben Cooper'
SITENAME = 'Ben Cooper'
THEME = 'flex-bkc'
SITEURL = 'https://bkcooper.github.io'

PATH = 'content'
STATIC_PATHS = ['images', 'static']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("Google Scholar", "https://scholar.google.com/citations?user=foQowpoAAAAJ&hl=en"),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False
PYGMENTS_STYLE = 'solarized-light'
TYPOGRIFY = True

# Flex specific stuff
# See https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings
SITETITLE = 'Ben Cooper'  # goes in the sidebar
# BROWSER_COLOR =
# USE_GOOGLE_FONTS = False   # True by default
# LINKS_IN_NEW_TAB = 'external'   # see docs


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
