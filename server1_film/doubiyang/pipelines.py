# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql



class DoubiyangPipeline(object):
    def open_spider(self,spider):
        self.connect = pymysql.connect(
            host='129.204.212.126',
            port=3306,
            user='root',
            password='520lzj',
            db='movie',
            charset='utf8'
        )
        self.conn = self.connect.cursor()

    def process_item(self, item, spider):
        source = item['source']
        film_name = item['film_name']
        title = item['title']
        real_url = item['real_url']
        self.connect.ping(reconnect=True)
        self.conn.execute("insert into ma_filmurl(source,film_name,title,url) values('%s','%s','%s','%s')"%(source,film_name,title,real_url))
        self.connect.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()
        self.connect.close()



class DetailPipeline(object):
    def open_spider(self,spider):
        self.connect = pymysql.connect(
            host='129.204.212.126',
            port=3306,
            user='root',
            password='520lzj',
            db='movie',
            charset='utf8'
        )
        self.conn = self.connect.cursor()

    def process_item(self, item, spider):
        film_name = item['film_name']
        type = item['type']
        detail_list = item['detail']
        img_url = item['img_url']
        self.connect.ping(reconnect=True)
        self.conn.execute("insert into ma_filmdetail values('%s','%s','%s','%s')"%(film_name,type,detail_list,img_url))
        self.connect.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()
        self.connect.close()
