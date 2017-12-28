# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/list-1-0.html']


    def parse(self, response):
        if 'http://www.xiaohuar.com/list-1' in response.url: 
            html = response.text

            img_urls = re.findall(r'/d/file/\d+/\w+\.jpg',html)
            for img_url in img_urls:
                if 'http://' not in img_url:
                    img_url =  'http://www.xiaohuar.com%s'% img_url
                yield Request(img_url) 
        else:
            url = response.url
            title = re.findall(r'(\w*.jpg)',url)[0]
            with open('/Users/vyoung/Desktop/doutu/%s' % title, 'wb') as f:
                f.write(response.body)
