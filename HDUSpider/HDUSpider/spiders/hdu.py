# -*- coding: utf-8 -*-
import scrapy

class HduSpider(scrapy.Spider):
    name = 'hdu'
    allowed_domains = ['acm.hdu.edu.cn']
    offset = 1000
    base_url = 'http://acm.hdu.edu.cn/showproblem.php?pid='
    start_urls = [base_url+str(offset)]
    
    def parse(self, response):
        
