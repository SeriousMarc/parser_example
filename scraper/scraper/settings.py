BOT_NAME = 'scraper'

SPIDER_MODULES = ['scraper.scraper.spiders']
NEWSPIDER_MODULE = 'scraper.scraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 300,
    'scraper.scraper.pipelines.ProductPipeline': 301
}

import os
IMAGES_STORE = ''

# LOG_LEVEL = 'ERROR'
LOG_LEVEL = 'DEBUG'

CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1

RANDOMIZE_DOWNLOAD_DELAY = True

COOKIES_ENABLED = True

AUTOTHROTTLE_ENABLED = True

AUTOTHROTTLE_DEBUG = False

try:
    from .local_settings import *
except ImportError:
    pass