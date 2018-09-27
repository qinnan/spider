from urllib import request
import ssl
import json

ssl._create_default_https_context=ssl._create_unverified_context

base_url = 'https://app.bxwst.com/wxZBX/sdk10671/24245.9PMETLEPA6BHNV50HKC1U63OH1OUDBF315359500610780.5873075488489121.758573824'
api_uri = '/wxZBX/appUser_pm_list?pageNo={page_no}&pm_type={pm_type}'
api_uri = api_uri.format(page_no='1', pm_type='1')
dst_url = base_url + api_uri
print(dst_url)
response = request.urlopen(dst_url)
obj_resp = json.loads(response.read().decode('utf-8'))
page_total = obj_resp['all_page']
for a in range(1, page_total):
    api_uri = '/wxZBX/appUser_pm_list?pageNo={page_no}&pm_type={pm_type}'
    api_uri = api_uri.format(page_no=a, pm_type=1)
    dst_url = base_url + api_uri
    response = request.urlopen(dst_url)
    obj_resp1 = json.loads(response.read().decode('utf-8'))
    for a in range(0, 10):
        faq_id = str(obj_resp1['data'][a]['id']).replace(',', '，').replace('\n', '')
        faq_question = str(obj_resp1['data'][a]['pm_title'])\
            .replace(',', '，').replace('\n', '').replace('?', '？').strip()
        faq_question_desc = str(obj_resp1['data'][a]['pm_desc']).replace('\n', '')
        out = faq_id + ',' + faq_question + ',' + faq_question_desc + ','
        print(out)
        with open('aaaa/q3list.txt', 'a', encoding='utf-8') as f:
           f.write(out + '\n')
