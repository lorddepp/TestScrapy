# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from doubanmovies.items import DoubanmoviesItem
from selenium import webdriver

class DoubanSpider(CrawlSpider):
    name = 'douban'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://movie.douban.com/top250']
    bro = webdriver.Edge(executable_path='msedgedriver.exe')

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+&filter='), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'https://movie.douban.com/subject/\d+/'), callback='parse_detail', follow=False),
    )

    def parse_item(self, response):
        pass

    def parse_detail(self,response):
        # 所需的response含有动态加载的数据，需使用selenium并修改中间件
        title = response.xpath('//div[@id="content"]/h1//text()').extract()[1].strip()
        desc = response.xpath('//div[@id="link-report"]/span[2]//text()').extract_first()
        img_src = response.xpath('//div[@id="mainpic"]/a/img/@src').extract_first()
        item = DoubanmoviesItem()
        item['title'] = title
        item['desc'] = desc
        item['img_src'] = img_src
        print(title,img_src)
        yield item

# scrapy crawl douban