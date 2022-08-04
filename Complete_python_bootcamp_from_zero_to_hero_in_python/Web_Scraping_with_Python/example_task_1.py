# Grabbing all elements of a class

import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup)

print(soup.select('.toctext'))

for item in soup.select('.toctext'):
    print(item.text)