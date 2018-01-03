# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HduspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    Input = scrapy.Field()
    Output = scrapy.Field()
    SampleInput = scrapy.Field()
    SampleOutput = scrapy.Field()
    #Author = scrapy.Field()
    time_limit = scrapy.Field()
    memory_limit = scrapy.Field()
    sourse = scrapy.Field()
    Recommend = scrapy.Field()
