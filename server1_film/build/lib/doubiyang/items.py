# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class DoubiyangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    film_name = scrapy.Field()
    source = scrapy.Field()
    title = scrapy.Field()
    real_url = scrapy.Field()



class Detail(scrapy.Item):
    film_name = scrapy.Field()
    type= scrapy.Field()
    detail = scrapy.Field()
    img_url = scrapy.Field()