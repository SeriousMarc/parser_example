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
from django.core.exceptions import FieldError

class ScraperPipeline(object):
    def process_item(self, item, spider):
        # save images
        
        # oc_product
        product_item = {k: v for k, v in item.items() if item[k]}

        # oc_product_description
        product_description_item = {}
        if product_item.get('description'):
            product_description_item.setdefault(
                'description', product_item.pop('description')
            )
        if product_item.get('name'):
            product_description_item.setdefault(
                'name', product_item.pop('name')
            )
        
        # oc_product_image
        product_image_item = {}
        if product_item.get('image_urls'):
            product_description_item.setdefault(
                'image_urls', product_item.pop('image_urls')
            )
        if product_item.get('images'):
            product_description_item.setdefault(
                'images', product_item.pop('images')
            )

        # oc_product_to_category
        product_category_item = {}
        if product_category_item.get('category'):
            product_description_item.setdefault(
                'category', product_item.pop('category')
            )


        try:
            # save oc_product
            product = OcProduct.objects.create(**product_item)
            if product:
                # save oc_product_description
                OcProductDescription.objects.create(
                    product_id=product.product_id,
                    **product_description_item
                )
        except FieldError:
            print('----------------------Item process failed-------------------------')
            raise DropItem()
        return item
