# -*- coding: utf-8 -*-
import scrapy
from HDUSpider.items import HduspiderItem  

class HduSpider(scrapy.Spider):
    name = 'hdu'
    allowed_domains = ['acm.hdu.edu.cn']
    base_url = "http://acm.hdu.edu.cn/showproblem.php?pid="
    offset = 1000
    start_urls = [base_url+str(offset)]
    def parse(self, response):
        #item = HduspiderItem()
        #node_list = response.xpath("//td[@align='center']")
        #title = node_list.xpath("//div[@class='panel_title']/text()").extract()
        #content = node_list.xpath("//div[@class='panel_content']")
        #print(title)
        #print(item)
        print("###############################")
        yield item
        if self.offset<6253:
            self.offset += 1
            url = self.base_url + str(self.offset)
            yield scrapy.Request(url,callback=self.parse)
