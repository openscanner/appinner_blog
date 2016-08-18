#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'AppInner'
SITENAME = "AppInner's Blog"
SITEURL = 'https://blog.appinner.com'
DEFAULT_LANG = 'en'

PATH = 'content'
OUTPUT_PATH = 'docs/'
TIMEZONE = 'Asia/Shanghai'

STATIC_PATHS = ['images', 'extra/favicon.ico', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}, 'extra/CNAME': {'path': 'CNAME'}}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
ARTICLE_LANG_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}-{lang}/index.html'

# Theme
THEME = 'pelican-themes/elegant'
HEADER_COLOR = 'black'
SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True
COLOR_SCHEME_CSS = 'github.css'  # code highlight

# Plugins
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["sitemap", "neighbors", "i18n_subsites"]  #

SITEMAP = {
    'format': 'txt',
}

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'cn': {
        'SITENAME': 'AppInner的博客',
        'SITEURL': 'https://blog.appinner.com/cn',
        'THEME': 'pelican-themes/elegant'
    }
}

# Blogroll
LINKS = (('Appinner', 'https://www.appinner.com/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/appinner'),
          ('facebook', 'https://www.facebook.com/appinner'),
          ('Email', 'mailto:support@appinner.com'))

TWITTER_URL = 'https://twitter.com/appinner'
FACEBOOK_URL = 'https://www.facebook.com/appinner'
GOOGLEPLUS_URL = ''

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# GOOGLE_ANALYTICS
