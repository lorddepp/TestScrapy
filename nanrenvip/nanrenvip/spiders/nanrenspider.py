# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from nanrenvip.items import NanrenvipItem
from selenium import webdriver
# from nanrenvip.items import NvyouItem

class NanrenspiderSpider(CrawlSpider):
    name = 'nanrenspider'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://nanrenvip.pw/nvyouku/1-0-0-0-0-0.html']
    bro = webdriver.Edge(executable_path='msedgedriver.exe')

    rules = (
        Rule(LinkExtractor(allow=r'/nvyouku/1-0-0-0-0-\d+.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/nvyouku/\w+.html'), callback='parse_page',follow=True),
        Rule(LinkExtractor(allow=r'/fanhaoku/\w+-\w+.html'), callback='parse_detail'),
    )

    def parse_item(self, response):
        pass
    def parse_page(self,response):
        pass
    def parse_detail(self,response):
        item = NanrenvipItem()
        name = response.xpath('//h4[@class="book-title"]//text()').extract()[0].split('#')[-2]
        # name = response.xpath('//p[@class="book-comment-p comment-p"]/text()').extract()[8][3:].split(',')
        title = response.xpath('//div[@class="novel-header"]/div/h1/text()').extract_first()
        img_src = 'http://'+response.xpath('//p[@class="cont_p"]/img/@src').extract_first()[2:]
        print('name: '+name,'title: '+title,'img: '+img_src)
        item['name'] = name
        item['title'] = title
        item['img_src'] = img_src
        yield item

# scrapy crawl nanrenspider