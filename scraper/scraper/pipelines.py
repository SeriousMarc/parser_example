# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import os
from shop_orm.models import (
    OcProduct, OcProductDescription, OcManufacturer, OcManufacturerDescription, 
    OcCategory, OcCategoryDescription, OcProductImage, OcProductToStore,
    OcProductToCategory
)
from scrapy.exceptions import DropItem
from django.core.exceptions import FieldError
from scraper.scraper.settings import IMAGES_STORE
from django.db import IntegrityError, transaction

class ProductPipeline(object):
    def process_item(self, item, spider):
        # save images
        print('-------------------PIPELINE--------------------------')
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
            product_image_item.setdefault(
                'image_urls', product_item.pop('image_urls')
            )
        if product_item.get('images'):
            product_image_item.setdefault(
                'images', product_item.pop('images')
            )

        # oc_product_to_category
        product_category_item = {}
        if product_item.get('category'):
            product_category_item.setdefault(
                'category', product_item.pop('category')
            )

        print('--------------------ITEM ITEM', item)
        print('--------------------PRODUCT_ITEM', product_item)
        print('--------------------PRODUCT_ITEM', product_description_item)
        try:
            # save oc_product
            saved_instances = []
            product = OcProduct.objects.create(**product_item)
            saved_instances.append(product)
            if product:
                # save oc_product_description
                product_d = OcProductDescription.objects.create(
                    product_id=product.product_id,
                    **product_description_item
                )
                saved_instances.append(product_d)
                product_store = OcProductToStore.objects.create(product_id=product.product_id)
                saved_instances.append(product_store)
                product_category = OcProductToCategory.objects.create(
                    product_id=product.product_id,
                    category_id=product_category_item.get('category')
                )

            if 'product_d' in locals() and product_d and product_image_item.get('images'):
                image_list = [
                    OcProductImage(
                        product_id=product_d.product_id,
                        image=os.path.join(
                            IMAGES_STORE, 
                            # re.search(r'\w+(?:\.\w+)*$', img['path']).group()
                            img['path']
                        )
                    )
                    for img in product_image_item['images']
                ]
                _msg = OcProductImage.objects.bulk_create(image_list)
        except Exception as e:
            print('----------------------Item saving process is failed-------------------------')
            for i in saved_instances:
                i.delete()
            if '_msg' in locals():
                print(_msg)
            print(e)
            raise DropItem()
        return item