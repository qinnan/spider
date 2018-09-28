import time
import os

result = []
with open(r'222 - 副本.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        result.append(line)
x = 0
total = result.__len__()
print(total)

title = ''
content = ''
# for x in range(0, total):
#     if result[x] != '----------\n':
#         print(result[x])
ss = ''
with open(r'222 - 副本.txt', mode='r', encoding='utf-8') as f:
    ss = f.read()
result = ss.split('----------\n')
# with open(r'finnal1.txt', mode='a', encoding='utf-8') as ff:
#     for a in result:
#         ccc = a.replace('\n', '')
#         ff.write(ccc)
#         ff.write('\n')
#         print(a)
with open(r'finnal1.txt', mode='r', encoding='utf-8') as ff:
    with open(r'finnal111.csv', mode='a', encoding='utf-8') as fff:
        for a in ff.readlines():
            x = a.replace(' ', ',', 1)
            print(x)
            fff.write(x)


