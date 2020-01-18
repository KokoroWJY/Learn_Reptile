from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, 'html.parser')


# get_text() 使用
nameList = bs.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())
print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

# 处理兄弟标签 next_siblings
for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)

# 处理子标签 孩子: children
for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)

# 处理子标签 后代: descendant
for descendant in bs.find('table', {'id': 'giftList'}).descendants:
    print(descendant)

# 处理父标签
print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())