# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import MySQLdb

class TencentspiderPipeline(object):
    def __init__(self):
        self.filename = open("tencent.json","w")
        #self.db = MySQLdb.connect("127.0.0.1","root",'',"NYOJ")

    def process_item(self, item, spider):
        text = json.dumps(dict(item),ensure_ascii = False)+ ', \n'
        self.filename.write(text.encode("utf-8"))
        #db = MySQLdb.connect("localhost","root",'',"NYOJ")
        #write into mysql
        #cursor = db.cursor()
       # sql = "insert into tencent(positionname,positionlink,positionType,peopleNum,workLocation,publishTime) values(%s,%s,%s,%s,%s,%s)" % (item['positionname'],item['positionlink'],item['positionType'],item['peopleNum'],item['workLocation'],item['publishTime'])
        #print(sql)
        #cursor.execute("insert into test(name,passwd) values('vyoung','123')")

        #db.commit()
       # db.close()
        return item

    def close_spider(self,spider):
        self.filename.close()
        #self.db.close()
