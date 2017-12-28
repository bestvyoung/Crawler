# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib2
from scrapy.http import Request
class XiaohuaPipeline(object):

    def process_item(self, item, spider):
        url = item['img_url']
        title = item['title']
        print(url)
        html = urllib2.urlopen(url).read()
        with open('/Users/vyoung/Desktop/doutu/%s.jpg' % title, 'wb') as f:    
            f.write(html)
        
        return item
