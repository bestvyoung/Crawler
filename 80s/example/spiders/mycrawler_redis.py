#-*- coding: UTF-8 -*-
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
import os
from scrapy_redis.spiders import RedisCrawlSpider
from example.items import ExampleItem

class MyCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'mycrawler_redis'
    redis_key = 'mycrawler:start_urls'

    node_link = LinkExtractor(allow=(r'movie/list/\w+----$'))
    node_page = LinkExtractor(allow=(r'movie/list/\w+-----\w-p\d+$'))
    moive_info = LinkExtractor(allow=(r'movie/\d+'))

    rules = (
        # follow all links
        Rule(node_link, callback='parse_page', follow=True),
        Rule(node_page,callback='deal_page',follow=True),
        Rule(moive_info,callback='deal',follow = False),
    )
    
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MyCrawler, self).__init__(*args, **kwargs)

    def mkdir(path):
        path = path.strip()
        path = path.rstrip("\\")
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            print("成功创建文件")
            return True
        else: 
            print("目录已存在")
            return False
    def parse_page(self, response):
        url = str(response.url)
        p_num = url[-5]
        name = response.xpath("//div[@class='f_block2']//dl[2]/ul/li[@id='genre%s']/a/text()" % p_num ).extract()[0].strip()
        print(name)
        path = "/Users/vyoung/Desktop/80s/"+name
        #print("gkjhgashkasjh")
        #path.decode('utf8')
        path = path.strip()
        isExists = os.path.exists(path)
        
        if not isExists:
            os.makedirs(path)
            

    def deal(self,response):
        item = ExampleItem() 
        item['img_url'] = response.xpath("//*[@id='minfo']/div[1]/img/@src").extract()[0]
        item['name'] = response.xpath("//*[@id='minfo']/div[2]/h1/text()").extract()[0]
        #item['actors'] = response.xpath("//*[@id='minfo']/div[2]/span[3]/a[1]/text()").extract()[0]
        item['category'] = response.xpath("//*[@id='minfo']/div[2]/div[1]/span[1]/a[1]/text()").extract()[0]
        item['area'] = response.xpath("//*[@id='minfo']/div[2]/div[1]/span[2]/a/text()").extract()[0]
        item['language'] = response.xpath("//*[@id='minfo']/div[2]/div[1]/span[3]/a/text()").extract()[0]
        item['director'] = response.xpath("//*[@id='minfo']/div[2]/div[1]/span[4]/a/text()").extract()[0]
        item['release_time'] = response.xpath("//*[@id='minfo']/div[2]/div[1]/span[5]/text()").extract()[0]
        item['play_time'] = response.xpath("//*[@id='minfo']/div[2]/div[1]/span[6]/text()").extract()[0]
        #item['synopsis'] = response.xpath("//*[@id='movie_content']/text()").extract()[0]
        item['score'] = response.xpath("//*[@id='minfo']/div[2]/div[2]/span[1]/text()").extract()[0].strip()
        item['download_url'] = response.xpath("//*[@id='myform']/ul/li[2]/span[3]/a/@href").extract()[0]
        #print(item)
        return item    

    def deal_page(self,response):
        pass
