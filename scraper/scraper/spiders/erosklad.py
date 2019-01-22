# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import ProductItem

class EroskladSpider(scrapy.Spider):
    name = 'erosklad'
    allowed_domains = ['erosklad.com']
    start_urls = ['https://erosklad.com/']

    # parse category
    def parse(self, response):
        links = response.xpath('//div[@class="left-nav__menu"]/div[1]/div/ul/li/a')
        for link in links:
            link_href = link.xpath('.//@href').extract_first()
            link_name = link.xpath('.//text()').extract_first()
            url = response.urljoin(link_href)
            request = scrapy.Request(url, callback=self.parse_category_filter)
            request.meta.setdefault('category_name', link_name)
            yield request

    def parse_category_filter(self, response):
        meta = {'category_name': response.meta['category_name']}
        links = response.xpath(
            '//span[@class="left-nav__menu-body-inside-title"]/following-sibling::ul/li/a'
        ).extract()
        if links:
            for link in links:
                link_href = link.xpath('.//@href').extract_first()
                link_name = link.xpath('.//text()').extract_first()
                url = response.urljoin(link_href)
                request = scrapy.Request(url, callback=self.parse_category_filter)
                meta.setdefault('filter_name', link_name)
                request.meta.update(meta)
                yield request
        
        #yield scrapy.Request(url, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        item = ProductItem()
        # oc_category
        item['category'] = response.meta['category_name']
        item['category_filter'] = response.meta['filter_name']

        links = response.xpath('//ul[@class="catalogue__list"]/li/div[1]/a/@href').extract()
        for link in links:
            url = response.urljoin(link)
            request = scrapy.Request(url, callback=self.parse_detail)
            request.meta.setdefault('item', item)
            yield request

        next_page = response.xpath(
            '//div[@class=" catalogue__header-bottom"]/ul/li[@class="next"]/a/@data-catalog-page'
        ).extract_first()
        if next_page:
            url = response.url + f"?page={next_page}"
            yield scrapy.Request(url, callback=self.parse_detail_page)
        
    def parse_detail(self, response):
        item = response.meta['item']
        
        card_gallery = response.xpath('//div[@class="item-card__gallery"]')
        card_info = response.xpath('//div[@class="item-card__info"]/div')

        # oc_product
        image = card_gallery.xpath('.//div[1]/div[1]/a/@href').extract_first()
        if image:
            item['image'] = image
        model = card_gallery.xpath(
            './/div[1]/div[2]/div[@class="item-card__short-info"]/div[1]/text()'
        ).extract_first()
        if model:
            model = model.replace(u'Артикул:', '').strip()
            item['model'] = model
        status_text = u'есть в наличии'
        status = card_gallery.xpath(
            './/div[1]/div[2]/div[@class="item-card__short-info"]/div[2]/div[1]/span/text()'
        ).extract_first()
        if status == status_text:
            item['status'] = 1 # есть в наличии
        else:
            item['status'] = 0 # нет в наличии
        options = [
            u'Диаметр': {'item': '', 'param': 'd'},
            u'Материал': {'item': '', 'param': 's'},
            u'Питание': {'item': '', 'param': 's'},
            u'Производитель': {'item': '', 'param': 's'},
            u'Длина': {'item': '', 'param': 'd'},
            u'Штрихкод': {'item': '', 'param': 'd'},
        ]
        for k, v in options:
            option = card_info.xpath(
                f'.//table/tbody/tr[contains(., "{k}")]/td[2]/text()'
            ).extract_first()
            re.sub(r'\D', '', price)
            if option:
                
            
        card_info.xpath('.//div[3]').extract_first()
        # oc_product_description
        name = card_gallery.xpath('//p[@class="item-card__title"]/text()').extract_first()
        if name:
            item['name'] = name
        desc = card_info.xpath('.//div[1]').extract_first()
        if desc:
            item['description'] = desc

        # oc_manufacturer


        yield item