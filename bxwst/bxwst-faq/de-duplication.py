# -*- coding:utf-8 -*-
import shutil
import os
import Levenshtein

def get_file_path():
    rootdir = r'D:\PycharmProjects\spider\bxwst\bxwst-faq\bbbb\q1'
    file_list = []
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
            #print(path)
            file_list.append(path)
    return file_list


# count = 0
# for a in get_file_path():
#     readDir = a
#     file_name = a.split('\\')[-1]
#     writeDir = r'D:\PycharmProjects\spider\bxwst\bxwst-faq\cccc\q1' + '\\' +file_name
#     lines_seen = set()
#     print(writeDir)
#     outfile = open(writeDir, "w", encoding='utf-8')
#     f = open(readDir, "r", encoding='utf-8')
#     first = f.readline()
#     outfile.write(first)
#     for line in f:
#         full_line = line
#         line_front = line.split(',')[0]
#         print(line)
#         if line_front not in lines_seen:
#             count += 1
#             outfile.write(full_line)
#             lines_seen.add(line_front)
#             print(a)
#             print('\n')
#     outfile.close()
#     print("success")
lines = dict()
for file in get_file_path():
    #print(file)
    with open(r'D:\PycharmProjects\spider\bxwst\bxwst-faq\bbbb\q1 - 副本\65岁糖尿病高血压病人是不是不能买保险.txt', encoding='utf-8') as f:
        tmp = f.read().splitlines()
        lines
for a in lines:
    print(a)