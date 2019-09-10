# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['1716dy.com']
    start_urls = ['https://www.1716dy.com/frim/index5.html','https://www.1716dy.com/frim/index6.html','https://www.1716dy.com/frim/index7.html']

    def parse(self, response):
        print('当前的url>>>>>>>>>>>>>>',response.url)
