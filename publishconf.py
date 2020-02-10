#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
# from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
AUTHOR = 'Ben Cooper'
SITENAME = 'Ben Cooper'
THEME = 'flex-bkc'
SITEURL = 'https://bkcooper.github.io'
RELATIVE_URLS = False

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

LINKS = (("Google Scholar", "https://scholar.google.com/citations?user=foQowpoAAAAJ&hl=en"),)

DEFAULT_PAGINATION = False
PYGMENTS_STYLE = 'solarized-light'
TYPOGRIFY = True

# Flex specific stuff
# See https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings
SITETITLE = 'Ben Cooper'  # goes in the sidebar
# BROWSER_COLOR =
# USE_GOOGLE_FONTS = False   # True by default
LINKS_IN_NEW_TAB = 'external'   # see docs

DELETE_OUTPUT_DIRECTORY = True  # careful!

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
