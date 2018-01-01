import scrapy
from scrapy.spider import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from TencentSpider.items import TencentspiderItem
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
class TencentSpider(CrawlSpider):
    name = "tencent"
    base_url = "hr.tencent.com/"
    allowed_domains = ["hr.tencent.com"]
    start_urls = ['http://hr.tencent.com/position.php?lid=&tid=&keywords=python&start=10#a']

    page_link = LinkExtractor(allow=("start=\d+"))
    new_link = LinkExtractor(allow=("detail"))
    #print(new_link)
    rules = [
        Rule(page_link ,callback="parseTencent",follow = True),
        Rule(new_link, callback="parse_page",follow = False)
    ]
    def parseTencent(self,response):
        db  = MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='NYOJ',charset='utf8')
        cursor = db.cursor()
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        
        for node in node_list:
            item = TencentspiderItem()
            item['positionname'] = str(node.xpath("./td[1]/a/text()").extract()[0])
            item['positionlink'] = str(node.xpath("./td[1]/a/@href").extract()[0])
            item['positionType'] = str(node.xpath("./td[2]/text()").extract()[0])
            item['peopleNum']  = str(node.xpath("./td[3]/text()").extract()[0])
            item['workLocation'] = str(node.xpath("./td[4]/text()").extract()[0])
            item['publishTime'] = str(node.xpath("./td[5]/text()").extract()[0])
            sql = """insert into tencent(positionname,positionlink,positionType,peopleNum,workLocation,publishTime) values('%s','%s','%s','%s','%s','%s')""" % (item['positionname'].encode("utf-8"),item['positionlink'].encode("utf-8"),item['positionType'].encode("utf-8"),item['peopleNum'].encode("utf-8"),item['workLocation'].encode("utf-8"),item['publishTime'].encode("utf-8"))
            #print(sql) 
            sql = "insert into test(name,passwd) values('vyoung ','12345')"
            cursor.execute(sql)
            db.commit()
            yield item
        db.close()
        
    def deal_link(self,links):
        for link in links:
            #print(link.url)
            link.url =  link.url
            #print(link.url)
        return links
    def parse_page(self,response):
        node_list = response.body
        print(node_list)
            
            #for node in node_list:
        #    content = node.xpath("./td/text()").extract()[0]
        #    print(content)

    def parse_item():
       # print(response.url)
       pass
