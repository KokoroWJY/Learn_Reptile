import scrapy

"""
ArticleSpider类和文件wikiSpider不一样,
表明这个类在wikiSpider的众多类目中专门用来抓取文章网页
"""


class ArticleSpider(scrapy.Spider):
    name = 'article'

    def start_requests(self):
        # 定义程序的入口, 用于生成Scrapy用来抓取网站的Request对象
        urls = [
            'http://en.wikipedia.org/wiki/Python_'
            '%28programming_language%29'
            'https://en.wikipedia.org/wiki/Functional_programming'
            'https://en.wikipedia.org/wiki/Monty_Python'
        ]
        return [scrapy.Request(url=url, callback=self.parse)
                for url in urls]

    def parse(self, response):
        # 是一个用户定义回调函数, 通过callback=self.parse传递给Request对象.
        url = response.url
        title = response.css('h1::text').extract_first()
        print("URL is: {}".format(url))
        print("Title is: {}".format(title))
