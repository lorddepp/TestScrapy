# -*- coding: utf-8 -*-
import scrapy
from FirstScrapy.items import FirstscrapyItem
from selenium import webdriver
# aaaaaaa
class TestscrapySpider(scrapy.Spider):
    name = 'testscrapy'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/domestic/']
    bro = webdriver.Edge(executable_path=r'D:\untitled\FirstScrapy\msedgedriver.exe')
    model_urls = []

    def parse(self, response):
        li_list = response.xpath('/html/body/div/div[3]/div[2]/div[2]/div/ul/li')
        model_index = [3,4]
        for index in model_index:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.model_urls.append(model_url)
            yield scrapy.Request(model_url,callback=self.model_parse)
    def model_parse(self,response):
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            page_url = div.xpath('./a/@href').extract_first()
            item = FirstscrapyItem()
            item['title'] = title
            yield scrapy.Request(page_url, callback=self.page_parse,meta={'item':item})
    def page_parse(self,response):
        item = response.meta['item']
        content = response.xpath('//*[@id="endText"]/p//text()').extract()
        content = ''.join(content)
        item['content'] = content
        yield item




