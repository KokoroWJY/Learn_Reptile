from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org'] # 保留的域名链接
    start_urls = ['http://en.wikipedia.org/wiki/Benevolent_dictator_for_life'] # 开始的链接
    # 正则表达式.*保留所有链接 rules为链接保留提供进一步的说明
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', folllow=True)]

    def parse_items(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        # xpath选择器 XPath通常用于获取包含子标签的文字内容
        text = response.xpath('//diiv[@id="mw-content-text"]//text()').extract()
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        lastUpdated = lastUpdated.replace('This page was last edited on ', '')
        print('URL is: {}'.format(url))
        print('title is: {}'.format(title))
        print('text is: {}'.format(text))
        print('Last updated: {}'.format(lastUpdated))