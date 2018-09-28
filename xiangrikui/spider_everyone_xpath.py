import requests
from bs4 import BeautifulSoup
from lxml import etree


url_list = []
with open('spider_url.txt', mode='r', encoding='utf-8') as f:
    for a in f.readlines():
        url_list.append(a)

url_list = ['http://www.xiangrikui.com/bxmingci/shehuibaoxian/20110112/85913.html']
for link in url_list:
    link = link.strip()
    print(link)
    response = requests.request('get', link)
    print(response.content.decode('gbk', "ignore"))
    html = etree.HTML(response.content)
    result = etree.tostring(html)
    
    break
