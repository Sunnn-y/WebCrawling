# import scrapy


# class NewsSpider(scrapy.Spider):
#     name = "news"
#     allowed_domains = ["naver.com"]
#     start_urls = ["https://naver.com"]

#     def parse(self, response):
#         print(response.text)
#         # pass


import scrapy
from study.items import StudyItem

class NewsSpider(scrapy.Spider):
    name = 'news'

    def start_requests(self):
        url = 'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=003'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        print(response.css('div.list_body > ul > li > dl > dt > a::attr(href)').getall())
