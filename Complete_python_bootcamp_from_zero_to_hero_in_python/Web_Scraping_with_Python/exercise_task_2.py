
# Get the names of all the authors on the first page.

import requests
import bs4

res = requests.get('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
authors = soup.select('.author')

author_names = set()

for author in authors:
    author_names.add(author.text)

print(author_names)