import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import sys

sys.path.append('F:/Python/python code/Learn_Reptile/wikiSpider/wikiSpider/')
from items import Article


class ArticleSpider(CrawlSpider):
    name = 'articleItems'
    allowed_domains = ['wikipedia.org']

    rules = [
        Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'),
             callback='parse_items', follow=True)
    ]

    def start_requests(self):
        start_urls = ['http://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'proxy': 'http://127.0.0.1:1080'})

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css('h1::text').extract_first()
        article['text'] = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        article['lastUpdated'] = lastUpdated.replace("This page was last edited on ','")
        return article
