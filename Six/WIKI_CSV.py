import csv
import requests
from bs4 import BeautifulSoup

proxies = {
    "http": "http://127.0.0.1:1080",
    'https': 'http://127.0.0.1:1080'
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
}

url = 'http://en.wikipedia.org/wiki/Comparison_of_text_editors'
html = requests.get(url, headers=headers, proxies=proxies, timeout=5)
bs = BeautifulSoup(html.text, 'html.parser')
table = bs.findAll('table', {'class': 'wikitable'})[0]
rows = table.findAll('tr')

csvFile = open('editors.csv', 'wt+')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
