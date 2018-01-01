# -- coding: utf-8 --
import scrapy
from scrapy.http import Request, FormRequest

class LoginSpider(scrapy.Spider):
    name = "login"
    #allowed_domains = ["xuzhougeng.top"]
          
    #向登录页发起请求，得到下一步需要的response
    def start_requests(self):
        return [Request('http://59.69.128.203/JudgeOnline/login.php', callback=self.post_login)] 

    ## 首先查看一下自己的状态，需要sign in。所以填写好表单，用FormRequest.from_response提交，这时候网页会返回一个重定向的response给我们，我们用after_login处理
    def post_login(self, response):
        #sign_in = response.xpath('//*[@id="navbar-collapse-01"]/ul[2]/li/a/text()').extract()[0]
        #print(sign_in)
        #csrf = response.css('div > input::attr(value)').extract_first()
        return FormRequest.from_response(response,formdata=
        {
                'userid':"1881140227",
                'password':'WWYhao110'
        },callback=self.after_login)
  ### 检查登录状态
    def after_login(self, response):
        with open("test.html", 'w') as f:
            f.write(response.body)

