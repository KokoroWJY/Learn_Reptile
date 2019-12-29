from bs4 import BeautifulSoup
import requests
import re
import random
import datetime

proxies = {
    "http": "http://127.0.0.1:1080",
    'https': 'http://127.0.0.1:1080'
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
}

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = requests.get('http://en.wikipedia.org{}'.format(articleUrl), headers=headers, proxies=proxies, timeout=5)
    bs = BeautifulSoup(html.text, 'html.parser')
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)