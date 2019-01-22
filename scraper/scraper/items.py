# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # oc_product
    model = scrapy.Field() # articul - sku
    image = scrapy.Field() # image url
    price = scrapy.Field()

    weight = scrapy.Field()
    length = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    
    status = scrapy.Field()
    date_added = scrapy.Field()
    date_modified = scrapy.Field()

    # oc_product_image
    images = scrapy.Field() # image urls

    # oc_product_description
    name = scrapy.Field()
    description = scrapy.Field()

    # oc_product_filter
    filters = scrapy.Field() # ask Andrew about filter table

    # oc_category
    category = scrapy.Field()
    category_filter = scrapy.Field()

    # oc_manufacturer
    manufacturer = scrapy.Field()
