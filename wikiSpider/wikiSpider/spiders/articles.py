from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org'] # 保留的域名链接
    start_urls = ['http://en.wikipedia.org/wiki/Benevolent_dictator_for_life'] # 开始的链接
    # 正则表达式.*保留所有链接 rules为链接保留提供进一步的说明
    rules = [
        # LinkEntractor 常用参数 allow:允许正则表达式. deny:拒绝正则表达式
        Rule(LinkExtractor(allow='^(/wiki/)((?!:).)*$'),
             callback='parse_items', follow=True,
             cb_kwargs={'is_article': True}),
        Rule(LinkExtractor(allow='.*'), callback='parse_items', cb_kwargs={'is_article': False})
    ]

    def parse_items(self, response, is_article):
        print(response.url)
        title = response.css('h1::text').extract_first()
        if is_article:
            # xpath选择器 XPath通常用于获取包含子标签的文字内容
            text = response.xpath('//diiv[@id="mw-content-text"]//text()').extract()
            lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
            lastUpdated = lastUpdated.replace('This page was last edited on ', '')
            print('title is: {}'.format(title))
            print('title is: {}'.format(title))
            print('text is: {}'.format(text))
        else:
            print('This is not an article: {}'.format(title))
            