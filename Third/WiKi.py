from bs4 import BeautifulSoup
import requests

proxies = {
    "http": "http://127.0.0.1:1080",
    'https': 'http://127.0.0.1:1080'
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
}
html = requests.get('https://en.wikipedia.org/wiki/Kein_Bacon', headers=headers, proxies=proxies, timeout=5)
bs = BeautifulSoup(html.text, 'html.parser')
print(bs.find_all('a'))
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

