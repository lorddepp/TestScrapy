# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
class NanrenvipPipeline(object):
    def process_item(self, item, spider):
        return item

class ImgPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):  # 用来对媒体资源进行请求的(数据下载)，参数item就是接收到的爬虫类提交的item对象
        yield scrapy.Request(item['img_src'],meta={'name':item['name'],'title':item['title']})
        # yield scrapy.Request(item['img_src'])

    def file_path(self, request, response=None, info=None):  # 指明数据存储的名称
        name = request.meta['name']
        title = request.meta['title']
        return u'{0}/{1}'.format(name,title+'.jpg')
        # 按标签
        # return u'{0}/{1}'.format(name,request.url.split('/')[-1])
        # return request.url.split('/')[-1]
        # for i in name:
        #     return u'{0}/{1}'.format(i, request.url.split('/')[-1])

    def item_completed(self, results, item, info):  # 将item传递个下一个即将被执行的管道类
        return item