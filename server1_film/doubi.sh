#! /bin/sh                                                                      
cd /root/lezhangjian/scrapy_doubi
nohup scrapy crawl doubi >> doubi.log 2>&1 &
