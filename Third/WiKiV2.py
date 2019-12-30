from bs4 import BeautifulSoup
import requests
import re

proxies = {
    "http": "http://127.0.0.1:1080",
    'https': 'http://127.0.0.1:1080'
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
}

pages = set()


def getLinks(pageUrl):
    global pages
    html = requests.get('http://en.wikipedia.org{}'.format(pageUrl), headers=headers, proxies=proxies, timeout=5)
    bs = BeautifulSoup(html.text, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/wiki)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # we have encountered a new page 我们会遇到一个新的页面
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks('')
