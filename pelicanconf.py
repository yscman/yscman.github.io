#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime

AUTHOR = 'Claudio Goncalves'
SITENAME = 'Data Log'
SITETITLE = "Data Log"
SITESUBTITLE = "My personal log on Python, R and other stuff"
SITEDESCRIPTION = "A data science and statistics blog"
SITEURL = 'https://yscman.github.io'

SITELOGO = '/images/selfie.jpeg'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"
DEFAULT_LANG = 'en'

PATH = 'content'
OUTPUT_PATH = "output"

TIMEZONE = 'America/New_York'

THEME = 'Flex'

ROBOTS = "index, follow"

PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = ['i18n_subsites']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}

FEED_ALL_ATOM = None
#FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = None
#CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

SOCIAL = (
    ("github", "https://github.com/yscman"),
    ("linkedin", "https://www.linkedin.com/in/cvgoncalves/"),
    ("twitter", "https://twitter.com/cvg_goncalves"),
    ("stack-overflow", "https://stackoverflow.com/users/13408448/vinny-cvg"),
    ("envelope", "mailto:cvg.goncalves@protonmail.com"),
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

DISQUS_SITENAME = "data log"
ADD_THIS_ID = "disqus_XSVEjw9R5B"

STATIC_PATHS = ["images", "extra/ads.txt", "extra/CNAME"]

EXTRA_PATH_METADATA = {
    "extra/ads.txt": {"path": "ads.txt"},
    "extra/CNAME": {"path": "CNAME"},
}

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True

# GOOGLE ANALYTICS
# For Google Analytics 4 use. Note that for old Google Analytics ('UA-XXXXX') the GOOGLE_ANALYTICS variable is included in publishconfig.py
# GOOGLE_GLOBAL_SITE_TAG = 'G-XXXXX'