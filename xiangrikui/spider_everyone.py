import requests
from bs4 import BeautifulSoup

url_list = []
with open('spider_url.txt', mode='r', encoding='utf-8') as f:
    for a in f.readlines():
        url_list.append(a)

url_list = ['http://www.xiangrikui.com/bxmingci/shehuibaoxian/20110112/85913.html']
for link in url_list:
    link = link.strip()
    print(link)
    response = requests.request('get', link)
    soup = BeautifulSoup(response.content, 'html.parser')

    right_tit = soup.find_all('div', class_='right_tit')
    ri_title_big = soup.find_all('div', class_='ri_title_big')
    ri_fill = soup.find_all('div', class_='ri_fill')
    title = ''
    content = ''
    if ri_title_big != '':
        title = ri_title_big
    else:
        title = right_tit
    content = ri_fill
    print(title)
    print(content)
