#pip install bs4
#pip install request
import requests
from bs4 import BeautifulSoup
url = 'https://www.codewithtomi.ml/'
r = requests.get(url)
print(r)
soup =BeautifulSoup(r.content,'lxml')
title = soup.find_all('h2',{'class':'post-title'})
print(title)
print(title.getText)
print(title[0].getText())
for t in title:
    print(t.getText())
