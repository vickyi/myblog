#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Dolphin Zhang'
SITEURL = 'http://honren.club'
SITENAME = "Dolphin Zhang's Blog"
SITETITLE = AUTHOR
SITESUBTITLE = 'Sotfware Engineer - Maker'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
# SITELOGO = '//s.gravatar.com/avatar/5dc5ba59a94eeab2106ad9d397361b2c?s=120'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

THEME = 'pelican-themes/Flex'
PATH = 'content'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'zh'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True

LINKS = (('Dolphin', 'http://honren.club'),)

# SOCIAL = (
#   ('linkedin', 'https://br.linkedin.com/in/alexandrevicenzi/en'),
#           ('github', 'https://github.com/alexandrevicenzi'),
#           ('google', 'https://google.com/+AlexandreVicenzi'),
#           ('twitter', 'https://twitter.com/alxvicenzi'),
#           ('rss', '//blog.honren.club/feeds/all.atom.xml')
#           )

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-D'
}

COPYRIGHT_YEAR = 2017

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap',]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# DISQUS_SITENAME = "alexandrevicenziblog"
# ADD_THIS_ID = 'ra-55adbb025d4f7e55'

STATUSCAKE = {
    'trackid': 'SL0UAgrsYP',
    'days': 7,
    'rumid': 6852,
    'design': 6,
}

STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}

CUSTOM_CSS = 'static/custom.css'

USE_LESS = True
