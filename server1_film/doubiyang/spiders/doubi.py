# -*- coding: utf-8 -*-
import scrapy
import json
from urllib.parse import unquote
import re
import time
import requests
from ..items import DoubiyangItem
import pymysql


class DoubiSpider(scrapy.Spider):
    name = 'doubi'
    allowed_domains = ['1716dy.com']
    start_urls = ['https://www.1716dy.com/frim/index5.html',
                  'https://www.1716dy.com/frim/index6.html',
                  'https://www.1716dy.com/frim/index7.html',
                  'https://www.1716dy.com/frim/index8.html',
                  'https://www.1716dy.com/frim/index9.html',
                  'https://www.1716dy.com/frim/index10.html',
                  'https://www.1716dy.com/frim/index11.html',
                  'https://www.1716dy.com/frim/index12.html',
                  ]

    def parse(self, response):
        next_url = 'https://www.1716dy.com'+response.xpath('/html/body/div[3]/div/div[2]/div[3]/ul/li[10]/a/@href').extract()[0]
        # print('next',next_url)
        yield scrapy.Request(url=next_url, callback=self.parse)
        detail_urls = ['https://www.1716dy.com' + u for u in response.xpath('/html/body/div[3]/div/div[2]/div[2]/div/ul/li/a/@href').extract()]
        for u in detail_urls:
            yield scrapy.Request(url=u, callback=self.get_indirect_url)


    def get_indirect_url(self, response):
        film_name = response.xpath('//div[@class="head"]/h3/text()').extract()[0]
        source = response.xpath('//*[@id="playlist"]/div/a/@title').extract()
        source_count = len(source)+1
        real_url_xpath = '//*[@id="playlist{}"]/ul/li/a/@href'
        real_title_xpath = '//*[@id="playlist{}"]/ul/li/a/@title'
        for i in range(1, source_count):
            index = i - 1
            title = response.xpath(real_title_xpath.format(i)).extract()
            indirect_urls = ['https://www.1716dy.com' + u for u in response.xpath(real_url_xpath.format(i)).extract()]
            if source[index] == '极速云播':
                for t,u in zip(title,indirect_urls):
                    yield scrapy.Request(url=u,callback=self.get_real_url_jisu,meta={'title':t,'source':source[index]+str(index),'film_name':film_name})

            if source[index] == '梨视频':
                for t, u in zip(title, indirect_urls):
                    yield scrapy.Request(url=u, callback=self.get_real_url_li,
                                         meta={'title': t, 'source': source[index]+str(index), 'film_name': film_name})


    def get_real_url_jisu(self, response):
        items = DoubiyangItem()
        real_urls = unquote(
            re.search(r'var now=unescape\("(.*?)"\);', response.text).groups(1)[0],
            'utf-8')
        real_urls = 'https://www.5mrk.com/m3u8.php?url=' + real_urls
        items['source'] = response.meta.get('source')
        items['title'] = response.meta.get('title')
        items['film_name'] = response.meta.get('film_name')
        items['real_url'] = real_urls
        # print('items是>>',items)
        yield items

    def get_real_url_li(self,response):
        items = DoubiyangItem()
        real_urls = unquote(
            re.search(r'var now=unescape\("(.*?)"\);', response.text).groups(1)[0],
            'utf-8')
        items['source'] = response.meta.get('source')
        items['title'] = response.meta.get('title')
        items['film_name'] = response.meta.get('film_name')
        items['real_url'] = real_urls
        # print('items是>>',items)
        yield items







