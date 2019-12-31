from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import random
import re
import datetime

proxies = {
    "http": "http://127.0.0.1:1080",
    'https': 'http://127.0.0.1:1080'
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
}

pages = set()

random.seed(datetime.datetime.now())


# 获取页面中所有内链的列表
def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []
    # 找出所有'/'开头的链接
    for link in bs.find_all('a', href=re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith('/')):
                    internalLinks.append(
                        includeUrl + link.attrs['href']
                    )
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks


# 获取页面中所有的外链链接
def getExternalLinks(bs, excluderUrl):
    externalLinks = []
    # 找出所有'http'或'www'开头且不包含当前URL的链接
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!' + excluderUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def getRandomExternalLink(startingPage):
    html = requests.get(startingPage, headers=headers, proxies=proxies, timeout=5)
    bs = BeautifulSoup(html.text, 'html.parser')
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print('No external links. looking around the site for one')
        domain = '{}://{}'.format(urlparse((startingPage).scheme, urlparse(startingPage).netloc))
        internalLinks = getInternalLinks(bs, domain)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is: {}'.format(externalLink))
    followExternalOnly(externalLink)


# 收集在网站上发现的所有的外链列表
allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = requests.get(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme, urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html.text, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)

allIntLinks.add('http://oreilly.com')
getAllExternalLinks('http://oreilly.com')


# followExternalOnly('http://oreilly.com')
