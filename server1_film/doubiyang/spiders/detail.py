# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import Detail
import re



class DetailSpider(scrapy.Spider):
    name = 'detail'
    allowed_domains = ['1716dy.com']
    start_urls = ['https://www.1716dy.com/frim/index4.html',
                  ]

    def parse(self, response):
        next_url = 'https://www.1716dy.com'+response.xpath('/html/body/div[3]/div/div[2]/div[3]/ul/li[10]/a/@href').extract()[0]
        # print('next',next_url)
        yield scrapy.Request(url=next_url, callback=self.parse)
        detail_urls = ['https://www.1716dy.com' + u for u in response.xpath('/html/body/div[3]/div/div[2]/div[2]/div/ul/li/a/@href').extract()]
        for u in detail_urls:
            yield scrapy.Request(url=u, callback=self.get_detail)

    def get_detail(self, response):
        Items = Detail()
        film_name = response.xpath('//div[@class="head"]/h3/text()').extract()[0]
        type = '动漫'
        detail_list = []
        detail_list.append(' '.join(response.xpath('//dd[@class="clearfix"]/ul/li[1]/a/text()').extract()))
        detail_list.append(' '.join(response.xpath('//dd[@class="clearfix"]/ul/li[2]/a/text()').extract()))
        detail_list.append(response.xpath('//dd[@class="clearfix"]/ul/li[3]/text()').extract()[0])
        detail_list.append(response.xpath('//dd[@class="clearfix"]/ul/li[4]/a/text()').extract()[0])
        detail_list.append(response.xpath('//dd[@class="clearfix"]/ul/li[5]/text()').extract()[0])
        detail_list.append(response.xpath('//dd[@class="clearfix"]/ul/li[6]/text()').extract()[0])
        detail_list = json.dumps(detail_list,ensure_ascii=False)
        img_url = response.xpath('//dl[@class="content"]/dt/a/@style').extract()[0]
        img_url = 'https://www.1716dy.comhttps://www.1716dy.com'+re.search(r'url\((.*?)\)',img_url).group(1)
        # print('电影名>>',film_name)
        # print('详情信息>>',detail_list)
        # print('图片地址>>',img_url)
        Items['film_name'] = film_name
        Items['type'] = type
        Items['detail'] = detail_list
        Items['img_url'] = img_url
        # print(detail_list)
        yield Items


