from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src': re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
for image in images:
    print(image['src'])