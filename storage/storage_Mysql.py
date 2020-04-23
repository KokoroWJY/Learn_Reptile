import requests
from bs4 import BeautifulSoup
import datetime
import random
import MySQLdb
import re

conn = MySQLdb.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='68dxqiji',
                       db='mysql_reptile', charset='utf8')
cur = conn.cursor()

random.seed(datetime.datetime.now())


def store(title, content):
    cur.execute('INSERT INTO pages (title, content) VALUES ("%s", "%s")', (title, content))
    cur.connection.commit()


def getLinks(articleUrl):
    proxies = {
        "http": "http://127.0.0.1:1080",
        'https': 'http://127.0.0.1:1080'
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }

    html = requests.get('http://en.wikipedia.org' + articleUrl, headers=headers, proxies=proxies)
    bs = BeautifulSoup(html.text, 'html.parser')
    title = bs.find('h1').get_text()
    content = bs.find('div', {'id': 'mw-content-text'}).find('p').get_text()
    store(title, content)
    return bs.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('/wiki/Kevin_Bacon')
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()
