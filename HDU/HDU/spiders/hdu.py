# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HduSpider(CrawlSpider):
    name = 'hdu'
    allowed_domains = ['acm.hdu.edu.cn']
    start_urls = ['http://acm.hdu.edu.cn/listproblem.php?vol=1']
    link_list = LinkExtractor(allow())
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
