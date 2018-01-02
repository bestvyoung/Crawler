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
        item = HduspiderItem()
        item['title'] = response.xpath("//tr[4]/td/h1/text()").extract()[0]
        item['description'] = response.xpath("//div[@class='panel_content'][1]/text()").extract()[0]
        title_input = response.xpath("//td[@align='center']/div[@class='panel_title'][2]/text()").extract()[0]
        if title_input == Input
            item['inputs'] = response.xpath("//div[@class='panel_content'][2]/text()").extract()[0]
        item['output'] = response.xpath("//div[@class='panel_content'][3]/text()").extract()[0]
        item['sample_input'] = response.xpath("//div[@class='panel_content'][4]/pre/div/text()").extract()[0]
        item['sample_output'] = response.xpath("//div[@class='panel_content'][5]/pre/div/text()").extract()[0]
        item['time_limit'] = response.xpath("//td[@align='center']/font/b/span/text()").extract()[0].split(' ')[2]+'MS'
        item['memory_limit'] = response.xpath("//td[@align='center']/font/b/span/text()").extract()[0].split(' ')[6] + 'K'
        item['sourse'] = 'HDU'
        print(item) 
        yield item
        if self.offset<6253:
            self.offset += 1
            url = self.base_url + str(self.offset)
            yield scrapy.Request(url,callback=self.parse)
