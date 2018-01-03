# -*- coding: utf-8 -*-
import scrapy
from HDUSpider.items import HduspiderItem  

class HduSpider(scrapy.Spider):
    name = 'hdu'
    allowed_domains = ['acm.hdu.edu.cn']
    base_url = "http://acm.hdu.edu.cn/showproblem.php?pid="
    offset = 1000
    start_urls = [base_url+str(offset)]
    def rep(self,string):
        return string.replace(' ','')
    def parse(self, response):
        item = HduspiderItem()
        node_list = response.xpath("//td[@align='center']")
        title = map(self.rep,node_list.xpath("//div[@class='panel_title']/text()").extract())
        content = node_list.xpath("//div[@class='panel_content']")
        item['time_limit'] = response.xpath("//td[@align='center']/font/b/span/text()").extract()[0].split(' ')[2]+'MS'
        item['title'] = response.xpath("//tr[4]/td/h1/text()").extract()[0]
        item['memory_limit'] = response.xpath("//td[@align='center']/font/b/span/text()").extract()[0].split(' ')[6] + 'K'
        item['sourse'] = 'HDU'
        item['description'] = response.xpath("//div[@class='panel_content'][1]/text()").extract()[0]

        for i in range(len(title)):
            if title[i] == 'Input':
                item['Input'] = content[i].xpath("./text()").extract()[0]
            if title[i] == 'Output':
                item['Output'] = content[i].xpath("./text()").extract()[0]
            if title[i] == 'SampleInput':
                item['SampleInput'] = content[i].xpath("./pre/div/text()").extract()[0]
            if title[i] == 'SampleOutput':
                item['SampleOutput'] = content[i].xpath("./pre/div/text()").extract()[0]
        print(item)
        #print("###############################")
        #yield item
        if self.offset<6253:
            self.offset += 1
            url = self.base_url + str(self.offset)
            yield scrapy.Request(url,callback=self.parse)
