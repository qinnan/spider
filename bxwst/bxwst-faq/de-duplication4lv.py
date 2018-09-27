import Levenshtein

a1 = '尊敬的客户，您好！建议您可以选择考虑我司康爱卫士老年防癌疾病有关产品。您可以登陆 http://baoxian.cntaiping.com/（太平网上商城）或拨打 400-868-8888（太平电话销售）；选择您需要的产品购买。祝您太平幸福！'
a2 = '尊敬的客户，您好！建议您可以选择考虑我司康爱卫士老年防癌疾病有关产品。您可以登陆 http://baoxian.cntaiping.com/（太平网上商城）或拨打 400-868-8888（太平电话销售）；选择您需要的产品购买。祝您太平幸福！'
print(Levenshtein.distance(a1, a2))