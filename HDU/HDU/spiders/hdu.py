# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from HDU.items import HduItem

class HduSpider(CrawlSpider):
    name = 'hdu'
    allowed_domains = ['acm.hdu.edu.cn']
    start_urls = ['http://acm.hdu.edu.cn/listproblem.php?vol=1']
    page_link = LinkExtractor(allow=(r'vol=\d+'))
    problem_link = LinkExtractor(allow=(r'pid=\d+'))
    rules = (
        Rule(problem_link,callback='node_deal',follow=False),
    )

    def parse_item(self, response):
        pass
        #print(response.url)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
    def link_deal(self,response):
        print(response.url)
    def node_deal(self,response):
        print("###############################################")
        items = HduItem()
        item['title'] = response.xpath("//tr[4]/td/h1/text()").extract()[0]
        item['description'] = response.xpath("//div[@class='panel_content'][1]/text()").extract()[0]
        item['inputs'] = response.xpath("//div[@class='panel_content'][2]/text()").extract()[0]
        item['output'] = response.xpath("//div[@class='panel_content'][3]/text()").extract()[0]
        item['sample_input'] = response.xpath("//div[@class='panel_content'][4]/pre/div/text()").extract()[0]
        item['sample_output'] = response.xpath("//div[@class='panel_content'][5]/pre/div/text()").extract()[0]
        item['time_limit'] = response.xpath("//td[@align='center']/font/b/span/text()").extract()[0].split(' ')[2]+'MS'
        item['memory_limit'] = response.xpath("//td[@align='center']/font/b/span/text()").extract()[0].split(' ')[6] + 'K'
        item['sourse'] = 'HDU'
        print(item)
        return item

