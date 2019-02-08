# -*- coding: utf-8 -*-
import scrapy
import re
import os
import wget
from ..items import ProductItem
from shop_orm.models import (
    OcProduct, OcCategory, OcCategoryDescription,
    OcManufacturer, OcManufacturerDescription
)
from datetime import datetime
from scraper.scraper.settings import IMAGE_DB_URL, IMAGES_STORE

DT_FORMAT = '%Y-%m-%d'


class EroskladSpider(scrapy.Spider):
    name = 'erosklad'
    allowed_domains = ['erosklad.com']
    start_urls = ['https://www.erosklad.com/authorization']
    
    # parse category
    def parse(self, response):
        return scrapy.FormRequest(
            'https://www.erosklad.com/authorization/check',
            formdata={
                '_target_path': '/',
                '_username': 'info1882@mail.ru', 
                '_password': '+Oo75055'
            },
            callback=self.parse_after_login
        )

    def parse_after_login(self, response):
        """parse main catogories"""
        # if "authentication failed" in response.body:
        #     self.logger.error("Login failed")
        #     return False
        links = response.xpath('//div[@class="left-nav__menu"]/div[1]/div/ul/li/a')
        for link in links:
            link_href = link.xpath('.//@href').extract_first()
            link_name = link.xpath('.//text()').extract_first()
            url = response.urljoin(link_href)

            request = scrapy.Request(url, callback=self.parse_category_filter)
            category = OcCategoryDescription.objects.filter(name=link_name).first()
            if category:
                request.meta.setdefault('category_id', category.category_id)
            else:
                category = OcCategory.objects.create()
                category_d = OcCategoryDescription.objects.create(
                    name=link_name, category_id=category.category_id
                )
                request.meta.setdefault('category_id', category_d.category_id)

            if request.meta.get('category_id'):
                yield request

    def parse_category_filter(self, response):
        """parse subcatogories"""
        links = response.xpath(
            '//span[@class="left-nav__menu-body-inside-title"]/following-sibling::ul/li/a'
        )
        if links:
            for link in links:
                link_href = link.xpath('.//@href').extract_first()
                link_name = link.xpath('.//text()').extract_first()
                url = response.urljoin(link_href)

                request = scrapy.Request(url, callback=self.parse_detail_page)
                category = OcCategoryDescription.objects.filter(name=link_name).first()
                if category:
                    request.meta.setdefault('category_id', category.category_id)
                else:
                    category = OcCategory.objects.create(parent_id=meta['category_id'])
                    category_d = OcCategoryDescription.objects.create(
                        name=link_name, category_id=category.category_id
                    )
                    request.meta.setdefault('category_id', category_d.category_id)

                if request.meta.get('category_id'):
                    yield request
        else:
            request = scrapy.Request(response.url, callback=self.parse_detail_page)
            request.meta.setdefault('category_id', response.meta['category_id'])
            if request.meta.get('category_id'):
                
                yield request 

    def parse_detail_page(self, response):

        products = response.xpath('//ul[@class="catalogue__list"]/li')
        
        # get price and sku
        # check if product exist in db
        for product in products:
            item = ProductItem()
            # oc_category
            item['category'] = response.meta['category_id']

            price = product.xpath(
                './/div[@class="catalogue__list-item-menu"]/span/text()'
            ).extract_first()
            price = int(re.sub(r'\D', '', price)) if price else None
            model = product.xpath('./div[2]/div[2]/p/text()').extract_first()
            
            p_instance = OcProduct.objects.filter(model=model).first()
            if p_instance:
                if price:
                    if price != int(p_instance.price):
                        p_instance.price = price
                        p_instance.date_mofidied = datetime.now().strftime(DT_FORMAT)
                    p_instance.status = 1 # есть в наличии
                else:
                    p_instance.status = 0
                p_instance.save()
                continue
            link = product.xpath('./div[1]/a/@href').extract_first()
            url = response.urljoin(link)
            request = scrapy.Request(url, callback=self.parse_detail)
            if price:
                item['price'] = price
                item['status'] = 1
            else:
                item['status'] = 0
            if model:
                item['model'] = model
            request.meta.setdefault('item', item)
            yield request

        next_page = response.xpath(
            '//div[@class=" catalogue__header-bottom"]/ul/li[@class="next"]/a/@data-catalog-page'
        ).extract_first()
        if next_page:
            url = response.url.split('?')[0] + "?page={}".format(next_page)
            request = scrapy.Request(url, callback=self.parse_detail_page)
            request.meta['category_id'] = response.meta['category_id']
            yield request
        
    def parse_detail(self, response):
        item = response.meta['item']

        card_gallery = response.xpath('//div[@class="item-card__gallery"]')
        card_info = response.xpath('//div[@class="item-card__info"]/div')

        # oc_product
        try:
            image = card_gallery.xpath('.//div[1]/div[1]/a/@href').extract_first()
            if image:
                if not os.path.exists(IMAGES_STORE):
                    os.makedirs(IMAGES_STORE)
                image_url = wget.download(
                    response.urljoin(image), 
                    IMAGES_STORE
                )
                if image_url:
                    item['image'] = os.path.join(
                        IMAGE_DB_URL, 
                        # re.search(r'\w+(?:\.\w+)*$', image_url).group()
                        re.search(r'[^/]+$', image_url).group()
                    )
        except Exception as e:
            print(e)
            return None
            
        # model = card_gallery.xpath(
        #     './/div[1]/div[2]/div[@class="item-card__short-info"]/div[1]/text()'
        # ).extract_first()
        # if model:
        #     model = model.replace(u'Артикул:', '').strip()
        #     item['model'] = model

        # status_text = u'есть в наличии'
        # status = card_gallery.xpath(
        #     './/div[1]/div[2]/div[@class="item-card__short-info"]/div[2]/div[1]/span/text()'
        # ).extract_first()
        # if status == status_text:
        #     item['status'] = 1 # есть в наличии
        # else:
        #     item['status'] = 0 # нет в наличии

        # oc_product_image

        image_urls = card_gallery.xpath('./div[@class="item-card__carousel"]/a/@href').extract()
        if image_urls:
            item['image_urls'] = [response.urljoin(url) for url in image_urls]

        # different oc_ tables
        options = {
            u'Диаметр': {'item': 'diameter', 'param': 'd'}, # d - decimal
            u'Материал': {'item': 'material', 'param': 's'}, # s - string
            u'Питание': {'item': 'power', 'param': 's'},
            u'Производитель': {'item': 'manufacturer', 'param': 's'},
            u'Длина': {'item': 'length', 'param': 'd'},
            u'Штрихкод': {'item': 'barcode', 'param': 'd'},
        }
        for k, v in options.items():
            if k == u'Производитель':
                option = card_info.xpath(
                    './/table/tbody/tr[contains(., "{}")]/td[2]/a/text()'.format(k)
                ).extract_first()
            else:
                option = card_info.xpath(
                    './/table/tbody/tr[contains(., "{}")]/td[2]/text()'.format(k)
                ).extract_first()
            if hasattr(item, v['item']) and option:
                option = option.strip()
                if v['param'] == 's':
                    setattr(item, v['item'], option)
                else:
                    setattr(item, v['item'], re.sub(r'\D', '', option))
        
        card_info.xpath('.//div[3]').extract_first()
        # oc_product_description
        name = card_gallery.xpath('//p[@class="item-card__title"]/text()').extract_first()
        if name:
            item['name'] = name
        desc = card_info.xpath('.//div[1]').extract_first()
        if desc:
            item['description'] = desc

        # oc_manufacturer
        if item.get('manufacturer'):
            manfac, m_created = OcManufacturer.object.get_or_create(name=item['manufacturer'])
            if m_created:
                OcManufacturerDescription.object.create(
                    manufacturer_id=manfac.manufacturer_id, 
                    name=manfac.name, 
                    meta_title=manfac.name
                )
            item['manufacturer'] = manfac.manufacturer_id
        print("-----------------------ITEM---------------------------")
        yield item