from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'dmoz'
    #allowed_domains = ['dmoz.org']
    start_urls = ['http://oj.ahstu.cc/JudgeOnline/problemset.php?page=1&v=pro']
    
    node_link = LinkExtractor(allow=("page=\d+"))
    rules = [
        Rule(node_link, callback='parse_directory', follow=True),
    ]

    def parse_directory(self, response):
        print(response.body)
        node_list = response.xpath("(//tr[@class='evenrow'] | //tr[@class='oddrow'])")
        for node in node_list:
            Id = node.xpath("./td[1]/div/text()").extract()[0]
            ti = node.xpath("./td[2]/div/a/text()").extract()[0]
            a = node.xpath("./td[4]/div/a/text()").extract()[0]
            sub = node.xpath("./td[5]/div/a/text()").extract()[0]
            rate = node.xpath("./td[6]/div/a/text()").extract()[0]
        yield {
            problem_id:"212",title:"1212",ac:"121",submit:"123",pass_rate:"123"
        }
