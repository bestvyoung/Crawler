from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider
from example.items import ExampleItem

class MyCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'mycrawler_redis'
    redis_key = 'mycrawler:start_urls'
    node_link = LinkExtractor(allow=(r'page=\d+&v=pro'))
    rules = (
        # follow all links
        Rule(node_link, callback='parse_page', follow=True),
    )

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MyCrawler, self).__init__(*args, **kwargs)

    def parse_page(self, response):
        node_list = response.xpath("(//tr[@class='evenrow'] | //tr[@class='oddrow'])")
        for node in node_list:
            item = ExampleItem()
            item['problem_id'] = node.xpath("./td[1]/div/text()").extract()
            item['title'] = node.xpath("./td[2]/div/a/text()").extract()
            item['ac'] = node.xpath("./td[4]/div/a/text()").extract()
            item['submit'] = node.xpath("./td[5]/div/a/text()").extract()
            item['pass_rate'] = node.xpath("./td[6]/div/a/text()").extract()
        #return {
        #    'name': response.css('title::text').extract_first(),
        #    'url': response.url,
        #}
            yield item
