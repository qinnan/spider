import requests
from pprint import pprint
import json


url = 'http://service.winbaoxian.com/askService/1/listAllAskQuestionFromCache?v=4.1.0&t=2&n=1&u=23127853%40winbaoxian.com&di=864035036715978&m=1&c=1'

req = requests.request(method='post', url=url)
response_content = str(req.content.decode('utf-8'))
json_content = json.loads(response_content, encoding='utf-8')

faq = json_content['r']['bigContentRecommendInfoList']
for a in faq:
    print(a['askQuestion']['title'])
