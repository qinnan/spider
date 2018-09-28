import requests
from bs4 import BeautifulSoup
import time

url_list = []
with open('spider_url.txt', mode='r', encoding='utf-8') as f:
    for a in f.readlines():
        url_list.append(a)

#url_list = ['http://www.xiangrikui.com/bxmingci/shehuibaoxian/20110112/85830.html']
#url_list = ['http://www.xiangrikui.com/bxmingci/changyong/20110121/88097.htmll']
with open('xiangrikui_knowlege.txt', mode='r', encoding='utf-8') as f:
    ff = open('333.txt', mode='a', encoding='utf-8')
    for link in url_list[0:]:
        link = link.strip()
        print(link)
        response = requests.request('get', link)
        time.sleep(2)
        soup = BeautifulSoup(response.content, 'html.parser')
        rt = soup.find_all('div', {'class': 'right_tit'})
        #rb = soup.find_all('div', {'class': 'ri_title_big'})
        #rf = soup.find_all('div', {'class': 'ri_fill'})
        aaa = soup.find_all(class_=['ri_title_big', 'ri_fill'])
        content = ''
        title = ''
        for x in range(0, aaa.__len__()):
            if aaa[x].attrs['class'][0] == 'ri_title_big':
                #sp = '----------\n'
                #print(sp)
                #ff.write(sp)
                title = aaa[x].text
                if aaa[x].text == '':
                    print(rt[0].get_text())
                    title = rt[0].get_text()
                print(title)
                ff.write('|' + title + '\n')
                continue
            if aaa[x].attrs['class'][0] == 'ri_fill':
                content = aaa[x].text
                ff.write('^' + content + '\n')
                print(content)
ff.close()
f.close()

# print(title)
# print(content)
