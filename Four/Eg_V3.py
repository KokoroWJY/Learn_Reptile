import requests
from bs4 import BeautifulSoup
from Eg_V2 import *


class Crawler:

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        """
        用于从一个BeautifulSoup对象和一个选择器获取内容的辅助函数.
        如果选择器没有找到对象, 就返回空字符串
        """
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    def parse(self, site, url):
        """
        从指定URL提取内容
        """
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()  # 调用print()方法


# 以下代码定义了网站对象并开启了流程
crawler = Crawler()
siteData = [
    ['O\'Rilly Media', 'http://oreilly.com', 'h1', 'section#product-description'],
    ['Reuters', 'http://reuters.com', 'h1', 'div.StandardArticleBody_body_1gnLA'],
    ['Brookings', 'http://www.brookings.edu', 'h1', 'div.post-body'],
    ['New Yourk Times', 'http://nytimes.com', 'h1', 'p.story-content']
]
websites = []
for row in siteData:
    websites.append(Website(row[0], row[1], row[2], row[3]))

crawler.parse(websites[0],
              'http://shop.oreilly.com/product/0636920028154.do')
crawler.parse(websites[1],
              'http://www.reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0')
crawler.parse(websites[2],
              'http://www.brookings.edu/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/')
crawler.parse(websites[3],
              'http://www.nytimes.com/2018/01/28/business/energy-environment/oil-boom.html')
