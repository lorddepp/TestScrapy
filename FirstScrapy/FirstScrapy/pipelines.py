# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class FirstscrapyPipeline(object):
    fp = None
    def open_spider(self, spider):  # 只会在爬虫开始的时候执行一次
        self.fp = open('./163news.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):  # 只在每次传item对象时调用一次
        title = item['title']
        content = item['content']
        self.fp.write(title+'\r\n'+content+'\r\n')
        print(title+'下载成功')
        return item  # return item的操作表示将item传递给下一个即将被执行的管道类

    def close_spider(self, spider):  # 只会在爬虫结束的时候调用一次
        self.fp.close()