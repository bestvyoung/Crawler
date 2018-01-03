# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class HduspiderPipeline(object):
    def __init__(self):
        self.db = MySQLdb.connect("forings.com","root","123456",jol)
        if self.db:
            print("connect success")
    def process_item(self, item, spider):
        cursor = db.cursor()
        sql = "insert into problem(title,description,input,output,sample_input,sample_out,sourse,time_limit,memory_limit) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (item['title'],item['description'],item['Input'],item['Output'],item['SampleInput'],item['SampleOutput'],item['sourse'],item['time_limit'],item['memory_limit'])
        return item
