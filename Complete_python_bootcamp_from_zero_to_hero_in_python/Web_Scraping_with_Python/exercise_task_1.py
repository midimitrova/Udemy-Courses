
# Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from the homepage.


import requests
import bs4

res = requests.get('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup)