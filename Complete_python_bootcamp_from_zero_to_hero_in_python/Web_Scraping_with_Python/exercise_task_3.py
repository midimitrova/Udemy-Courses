
# Create a list of all the quotes on the first page.

import requests
import bs4

res = requests.get('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
quotes = soup.select('.text')

quotes_list = []

for quote in quotes:
    quotes_list.append(quote.text)
print(quotes_list)