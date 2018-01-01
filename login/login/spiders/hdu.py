# -- coding: utf-8 --
import scrapy
from scrapy.http import Request, FormRequest

class LoginSpider(scrapy.Spider):
    name = "login"
    #allowed_domains = ["xuzhougeng.top"]
    headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
    "Connection": "keep-alive",
    "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    "Referer":"http://acm.hdu.edu.cn/"

    }

    #向登录页发起请求，得到下一步需要的response
    def start_requests(self):
        return [Request('http://acm.hdu.edu.cn/userloginex.php?action=login', callback=self.post_login)] 

    ## 首先查看一下自己的状态，需要sign in。所以填写好表单，用FormRequest.from_response提交，这时候网页会返回一个重定向的response给我们，我们用after_login处理
    def post_login(self, response):
        #sign_in = response.xpath('//*[@id="navbar-collapse-01"]/ul[2]/li/a/text()').extract()[0]
        #print(sign_in)
        #csrf = response.css('div > input::attr(value)').extract_first()
        return FormRequest.from_response(response,headers = self.headers,formdata=
        {
                'username':"1881140227",
                'userpass':'WWYhao110',
                'login': 'Sign In'
        },callback=self.after_login)
  ### 检查登录状态
    def after_login(self, response):
        with open("test.html", 'w') as f:
            f.write(response.body)

