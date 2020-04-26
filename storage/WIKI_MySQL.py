from bs4 import BeautifulSoup
import requests
import re
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd='68dxqiji',
                       db='wikipedia', charset='utf8')
cur = conn.cursor()


def insertPageIfNotExists(url):
    cur.execute('SELECT * FROM `pages` WHERE `url` = (%s)', url)
    if cur.rowcount == 0:
        cur.execute('INSERT INTO `pages` (`url`) VALUES (%s)', url)
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]


def loadPages():
    cur.execute('SELECT * FROM `pages`')
    pages = [row[1] for row in cur.fetchall()]
    return pages


def insertLink(fromPageId, toPageId):
    cur.execute('SELECT * FROM `links` WHERE `fromPageId` = %s AND `toPageId` = %s', (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO `links` (`fromPageId`, `toPageId`) VALUES (%s, %s)', (int(fromPageId), int(toPageId)))
        conn.commit()


def pageHasLinks(pageId):
    cur.execute('SELECT * FROM `links` WHERE `fromPageId` = %s', (int(pageId)))
    rowcount = cur.rowcount
    if rowcount == 0:
        return False
    return True


def getLinks(pageUrl, recursionLevel, pages):
    if recursionLevel > 4:
        return

    pageId = insertPageIfNotExists(pageUrl)
    html = requests.get('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html.text, 'html.parser')
    links = bs.findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    links = [link.attrs['href'] for link in links]

    for link in links:
        linkId = insertPageIfNotExists(link)
        insertLink(pageId, linkId)
        if not pageHasLinks(linkId):
            print("PAGE HAS NO LINKS: {}".format(link))
            pages.append(link)
            getLinks(link, recursionLevel + 1, pages)


getLinks('/wiki/Kevin_Bacon', 0, loadPages())
cur.close()
conn.close()
