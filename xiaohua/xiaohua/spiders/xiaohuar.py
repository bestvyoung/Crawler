# -*- coding: utf-8 -*-
import scrapy
import re
from xiaohua.items import XiaohuaItem
from scrapy.http import Request
class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    allowed_domains = ['xiaohuar.com']
    base_url = "http://www.xiaohuar.com/list-1-"
    offset = 33
    start_urls = [base_url+str(offset)+'.html']


    def parse(self, response):
        node_list  = response.xpath("//div[@id = 'list_img']//img")
        for node in node_list:
            item = XiaohuaItem()
            url = node.xpath("./@src").extract()[0]
            url = str(url)
            #print(url)
            url = "http://www.xiaohuar.com%s" % url
            item['img_url'] = url
            item['title'] = node.xpath("./@alt").extract()[0]
            yield item
        
        if self.offset<43:
            self.offset += 1
            url = self.base_url + str(self.offset) + '.html'
            yield scrapy.Request(url,callback=self.parse) 

