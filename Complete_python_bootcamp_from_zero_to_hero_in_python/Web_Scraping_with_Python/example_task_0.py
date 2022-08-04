# Grabbing the title of a page

import requests
import bs4

res = requests.get('https://www.example.com/')
print(res.text)

soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup)
print(soup.select('title'))
print(soup.select('title')[0].text)
