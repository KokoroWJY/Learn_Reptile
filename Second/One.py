from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())
# print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

# for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
#     print(sibling)

# for child in bs.find('table', {'id': 'giftList'}).children:
#     print(child)
