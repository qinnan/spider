import requests


url = 'https://baike.baidu.com/item/{company}'
url = url.format(company='平安保险')
url = 'https://www.baidu.com/s?wd=平安保险'
print(url)
rep = requests.request('get', url=url, AllowRedirect=True)
print(rep.content)