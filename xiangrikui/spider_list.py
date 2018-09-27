import requests
import json
import ssl
from bs4 import BeautifulSoup

url = 'http://www.xiangrikui.com/bxmingci/'
response = requests.request('get', url=url)
soup = BeautifulSoup(response.content, 'html.parser')
for link in soup.find_all('a'):
    with open('spider_url.txt', mode='a', encoding='utf-8') as f:
        f.writelines(link.get('href') + '\n')
        print(link.get('href'))
    f.close()
