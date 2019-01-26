import os, scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from django.core.management.base import BaseCommand, CommandError

from scraper.scraper import spiders


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        os.environ['SCRAPY_PROJECT'] = 'sexshop'
        process = CrawlerProcess(get_project_settings())
        process.crawl(spiders.erosklad.EroskladSpider)
        process.start()