import time
import os

result = []
with open(r'D:\PycharmProjects\spider\xiangrikui\222 - 副本.txt',
          mode='r', encoding='utf-8') as f:
    for line in f:
        result.append(line)
x = 0
total = result.__len__()
print(total)

title = ''
content = ''
for x in range(0, total):
    if result[x] == '----------\n':
        print(result[x + 1])
