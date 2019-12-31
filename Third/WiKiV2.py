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

pages = set()  # 全局变量集合(已抓取的变量集合)


def getLinks(pageUrl):
    global pages
    html = requests.get('http://en.wikipedia.org{}'.format(pageUrl), headers=headers, proxies=proxies, timeout=5)
    bs = BeautifulSoup(html.text, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print("页面缺少一页, 不用担心!")

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPages = link.attrs['href']
                print('-' * 20)
                print(newPages)
                pages.add(newPages)
                getLinks(newPages)


getLinks('')
