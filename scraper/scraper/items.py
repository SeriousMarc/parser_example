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

    sku = scrapy.Field()
    #THIS FIELD IS ONLY FOR TEST
    #AND WILL ALWAYS EQUAL TO 'TEST'
    #TO LET YOU REMOVE ALL PRODUCTS WITH SKU=TEST

    # oc_product_image
    image_urls = scrapy.Field()
    images = scrapy.Field() # image urls

    # oc_product_description
    name = scrapy.Field()
    description = scrapy.Field()

    # oc_product_filter
    filters = scrapy.Field() # ask Andrew about filter table

    # oc_category
    category = scrapy.Field()

    # oc_manufacturer
    manufacturer = scrapy.Field()

    #for sqlalchemy
    # default_field_values = {
    #     'model': '', 'sku': '', 'upc': '', 'ean': '', 'jan': '',
    #     'isbn': '', 'mpn': '', 'location': '', 'stock_status_id': 0, 'image': '', 
    #     'manufacturer_id': 0, 'price': 0, 'tax_class_id': 0, 'weight': 0, 'length': 0, 
    #     'width': 0, 'height': 0, 'date_added': '0000-00-00', 'date_modified': '0000-00-00'
    # }