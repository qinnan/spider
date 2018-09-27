import os

file_path = r'D:\PycharmProjects\spider\faqtxt\150.txt'
fo = open(file_path, mode='r', encoding='utf-8')
line = fo.readline()
while line:
    if line.find('.') != -1:
        print(line)
    line = fo.readline()
fo.close()
