# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from shop_orm.models import (
    OcProduct, OcProductDescription, OcManufacturer, OcManufacturerDescription, 
    OcCategory, OcCategoryDescription, OcProductImage
)
from scrapy.exceptions import DropItem
class ScraperPipeline(object):
    def process_item(self, item, spider):
        # get all not empty and only for product items
        product_item = {k: v for k, v in item.items() if item[k]}

        # save images

        # save product

        raise DropItem()

        return item
