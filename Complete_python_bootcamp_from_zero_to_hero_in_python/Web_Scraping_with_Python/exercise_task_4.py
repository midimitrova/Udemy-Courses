
# Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from
# the home page (e.g Love,Inspirational,Life, etc...)


import requests
import bs4

res = requests.get('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
tags = soup.select('.tag-item')

tags_list = []

for tag in tags:
    tags_list.append(str.strip(tag.text))
print(tags_list)