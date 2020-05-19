# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class DoubanmoviesPipeline(object):
    fp = None
    def open_spider(self, spider):  # 只会在爬虫开始的时候执行一次
        self.fp = open('./movies.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):  # 只在每次传item对象时调用一次
        title = item['title']
        desc = item['desc']
        self.fp.write(title+':'+desc)
        return item  # return item的操作表示将item传递给下一个即将被执行的管道类

    def close_spider(self, spider):  # 只会在爬虫结束的时候调用一次
        self.fp.close()

class ImgPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_src'],meta={'title':item['title']})

    def file_path(self, request, response=None, info=None):
        title = request.meta['title']
        return u'{0}.jpg'.format(title)

    def item_completed(self, results, item, info):
        return item