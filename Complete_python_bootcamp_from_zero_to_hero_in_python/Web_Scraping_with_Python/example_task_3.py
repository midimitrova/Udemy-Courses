# Getting an Image from a Website

import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup)
image_info = soup.select('.image')
# print(image_info)
women = image_info[0]
print(women)

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Commodore_Grace_M._Hopper%2C_USN_%28covered%29.jpg/220px-Commodore_Grace_M._Hopper%2C_USN_%28covered%29.jpg')
# print(image_link.content)

f = open('my_new_file.jpg', 'wb')
f.write(image_link.content)
f.close()