#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://matheusfrancisco.github.io/'
#RELATIVE_URLS = False

#FEED_DOMAIN = SITEURL
#FEED_ALL_ATOM = ''
#CATEGORY_FEED_ATOM = ''

#SOCIAL = SOCIAL + (('rss', SITEURL + '/' + FEED_ALL_ATOM),)

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "matheus-francisco"
DISQUS_SHORTNAME = "matheus-francisco"
DISQUS_DISPLAY_COUNTS = True

#GOOGLE_ANALYTICS = ""
