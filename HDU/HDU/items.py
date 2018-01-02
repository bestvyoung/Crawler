# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    inputs = scrapy.Field()
    output = scrapy.Field()
    sample_input = scrapy.Field()
    sample_output = scrapy.Field()
    time_limit = scrapy.Field()
    memory_limit = scrapy.Field()
    sourse = scrapy.Field()
