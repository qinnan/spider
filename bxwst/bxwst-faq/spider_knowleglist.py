from urllib import request
import ssl
import json
import os

ssl._create_default_https_context=ssl._create_unverified_context

base_url = 'https://app.bxwst.com/wxZBX/sdk10671/public/wxZBX/appUser_knowledgeList'
for a in range(58, 67):
    api_uri = '?knowledge_label_id={label_id}'
    api_uri = api_uri.format(label_id=a)
    dst_url = base_url + api_uri
    #print(dst_url)
    response = request.urlopen(dst_url)
    obj_resp = json.loads(response.read().decode('utf-8'))
    #print(obj_resp)
    for b in obj_resp['data']:
        #print(b['knowledge_id'], b['knowledge_title'])
        knowledge_detail_url = 'https://app.bxwst.com/wxZBX/sdk10671/public/wxZBX/appUser_knowledge_detail?knowledge_id={knowledge_id}'
        rsp = request.urlopen(knowledge_detail_url.format(knowledge_id=b['knowledge_id']))
        detail_json = json.loads(rsp.read().decode('utf-8'))
        knowledge_title = detail_json['data']['knowledge_title']
        knowledge_content = detail_json['data']['knowledge_content']
        knowledge_title = str(knowledge_title)\
            .replace(',', '，').replace(r"\r\n", "").replace('?', '？')
        knowledge_content = str(detail_json['data']['knowledge_content'])\
            .replace(',', '，').replace('?', '？').replace(r"\r\n", "")
        print(knowledge_detail_url.format(knowledge_id=b['knowledge_id']))
        print(knowledge_title)
        fo = open('faqtxt\\aaaa.txt'.format(knowledge_title=b['knowledge_id']), 'a', encoding='utf-8')
        #print(out)
        out = knowledge_title + ','
        out += knowledge_content + '\n'
        fo.writelines(out)
        fo.close()
