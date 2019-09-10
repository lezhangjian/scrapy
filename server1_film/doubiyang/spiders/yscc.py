# -*- coding: utf-8 -*-
import scrapy


class YsccSpider(scrapy.Spider):
    name = 'yscc'
    allowed_domains = ['757ys.cc']
    start_urls = ['https://www.757ys.cc/f/vod/index.html']
    count = 1

    def parse(self, response):
        page_url = response.xpath('//div[@class="page clearfix"]/a[@class="pagelink_b"]/@href').extract()
        for url in page_url:
            real_url = 'https://www.757ys.cc'+url
            yield scrapy.Request(url=real_url, callback=self.parse)
        film_detail_url = response.xpath('//div[@class="index-area clearfix"]/ul/li/a/@href').extract()
        for urls in film_detail_url:
            detail_url = 'https://www.757ys.cc'+urls
            yield scrapy.Request(url=detail_url, callback=self.detail_url_parse)

    def detail_url_parse(self, response):
        film_urls = response.xpath('//div[@id="vlink_1"]/ul/li/a/@href').extract()
        title = response.xpath('//div[@id="vlink_1"]/ul/li/a/@title').extract()
        for url in film_urls:
            film_url = 'https://www.757ys.cc'+url
            yield scrapy.Request(url=film_url, callback=self.real_url_parse)

    def real_url_parse(self, response):
        pass
    'https://www.757ys.cc/jiexi/index.php?url=http://www.mgtv.com/b/156864/1771520.html'
    'https://www.757ys.cc/jiexi/index.php?url=http://www.mgtv.com/b/156864/1771520.html'
    '/jiexi/index.php?url='+MacPlayer.PlayUrl+''


