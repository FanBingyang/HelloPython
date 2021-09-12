# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  compare.py    
@Time   :  2020/6/6 9:44 
@Author :  ByFan
'''
import os


def readLines(filepath):
    lines = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception:
        with open(filepath, 'r', encoding='gbk') as f:
            lines = f.readlines()
    return lines


def compare(file1, file2):
    lines1 = readLines(file1)
    lines2 = readLines(file2)

    count = 0.
    for line in lines1:
        if lines2.count(line) > 0:
            count += 1
    return count / max(len(lines1), len(lines2))


# path = "第二次作业"  # 输入路径，根据实际情况决定。
# dirs = os.listdir(path)
# files = []
# error_files = []
# for file in dirs:
#     files.append(os.path.join(path, file))

# for i in range(len(files)):
#     for j in range(i + 1, len(files)):
if __name__=="__main__":
    try:
        degree = compare("F:\\QQ接收\\思政论文.doc", "F:\\QQ接收\\思政论文(2).doc")
        print(degree)
        # if degree > 0.7:
            # print("{}和{}的作业相似度为：{:.2%}".format(files[i].split(" ")[0], files[j].split(" ")[0], degree).replace(
            #     "第二次作业\\", ""))
    except Exception as e:
        # if error_files.count(j) == 0:
        #     error_files.append(j)
        pass
        # continue