# -*- coding: utf-8 -*-
AUTHOR = 'xidada9888'
SITENAME = '河北考试网'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'zh'

# 文章与页面设置
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 'css', 'js']

# 分类与标签
DISPLAY_CATEGORIES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = True

# 主题（先用默认，后续可换）
THEME = 'notmyidea'

# 插件配置
PLUGIN_PATHS = ['plugins']
PLUGINS = ['seo', 'sitemap']

# SEO设置
SEO_REPORT = True
SEO_ENHANCER = True
SEO_ENHANCER_OPEN_GRAPH = True
SEO_ENHANCER_TWITTER_CARDS = True

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# 默认文章状态为草稿
DEFAULT_STATUS = 'draft'

# 创建文章目录
import os
if not os.path.exists('content/articles'):
    os.makedirs('content/articles')