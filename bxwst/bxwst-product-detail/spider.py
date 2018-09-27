import requests
from pprint import pprint
import json
import ssl


ssl._create_default_https_context = ssl._create_unverified_context
def get_product_id():
    # for a in range(1, 12):
    host = 'https://app.bxwst.com'
    #product_list_uri = 'wxZBX/sdk10671/undefined/wxZBX/appUser_product_discount_list?page={page}&pcid={pcid}'
    product_list_uri = '/wxZBX/sdk10671/24247.MPP2G9TO76D3M34D0N753JS65RI3SUOL15374940257980.7122735052835196.479624978/wxZBX/appUser_product_discount_list?page={page}&pcid={pcid}'
    url = host + product_list_uri.format(page='4', pcid='5')
    print(url)
    req = requests.request(method='get', url=url)
    req = req.content.decode('utf-8')
    json_req = json.loads(req)
    pprint(json_req)


def get_product_detail():
    pass;


get_product_id()
