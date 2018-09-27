from urllib import request
import ssl
import json
import math

ssl._create_default_https_context = ssl._create_unverified_context

base_url = 'https://app.bxwst.com/wxZBX/sdk10671/24641.TU2CJU4MSUF695Q637F4268MO1OVU37915359602837130.554856515256688.229143457'
api_uri = '/wxZBX/appUser_rp_info?pm_id={pm_id}&pageNo={page_no}'
fo = open('aaaa/q1list.txt', encoding='utf-8')
get_count_url = 'https://app.bxwst.com/wxZBX/sdk10671/24641.S7RL84AEON5T0PKM6TSLMQ9BA2KE3MQ115359623459650.7835654276423156.481094535/wxZBX/appUser_pm_info?pm_id={pm_id}'

id_list = []
for a in fo.readlines():
    a = a.split(',')
    one = {'id': a[0], 'question': a[1], 'question_desc': a[2]}
    print(a[0], a[1], a[2])
    id_list.append(one)
fo.close()
# for a in id_list:
#     print(a.get('id'), a.get('question'), a.get('question_desc'))
num = 1;
for aa in id_list:
    fo = open('bbbb\q1\{question}.txt'.format(question=aa.get('question')), 'a', encoding='utf-8')
    response = request.urlopen(get_count_url.format(pm_id=aa.get('id')))
    obj_resp = json.loads(response.read().decode('utf-8'))
    answer_count = obj_resp['data'][0]['count']
    question = obj_resp['data'][0]['pm_title']
    print(str(num) + '-' + question)
    num += 1
    fo.write(question + '\n')
    fo.write(str(aa.get('question_desc')) + '\n')
    for xx in range(1, math.ceil(answer_count / 10.0)):  # 获取分页
        dst_url = base_url + api_uri.format(pm_id=aa.get('id'), page_no=xx)
        response = request.urlopen(dst_url)
        obj_resp = json.loads(response.read().decode('utf-8'))
        for yy in range(0, 10):  # 获取每页
            user_appraise = obj_resp['data'][yy]['user_appraise']
            pm_desc = str(obj_resp['data'][yy]['pm_desc']).replace('\n', '')
            if user_appraise is None:
                user_appraise = '0'
            #abc = '{pm_desc},{user_appraise}'.format(user_appraise=user_appraise, pm_desc=pm_desc)
            abc = '{pm_desc}'.format(pm_desc=pm_desc)
            #print('{pm_desc},{user_appraise}'.format(user_appraise=user_appraise, pm_desc=pm_desc))
            #print('{pm_desc}'.format(pm_desc=pm_desc))
            fo.write(abc + '\n')
    fo.close()
