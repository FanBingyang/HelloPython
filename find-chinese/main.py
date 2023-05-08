# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  main.py    
@Desc   :  寻找汉字
@Author :  byfan
@Time   :  2022/10/11 15:08 
'''

from byfanTranslate import translate
import os
import re


def findFile(rootDir):
    for root, dirs, files in os.walk(rootDir):
        print("当前路径 ===>", root)
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        # print("\t所有文件:")
        for f in files:
            # print("\t\t", os.path.join(root, f))
            fullPath = os.path.join(root, f)
            openFile(fullPath)
        # 遍历所有的文件夹
        # print("\t所有文件夹:")
        # for d in dirs:
        #     print(os.path.join(root, d))


def openFile(filePath):
    list = []
    file_name = filePath[filePath.rindex("/")+1:]
    # file_name = "test.java"
    list.append("========> "+file_name)
    file_object = open(filePath, 'r')
    dirPath = filePath[:filePath.rindex("/")]

    resultFile = dirPath[dirPath.rindex("/")+1:] + ".txt"

    lines = file_object.readlines()
    for i, line in enumerate(lines):
        flag, chinese = matchChinese(line)
        if flag:
            # print(str(i+1) + " = " + line)
            translate_result = str(translate(chinese))
            msg = "\t" + str(i+1) + " :\t" + chinese + "\n\t\t\t"
            key = translate_result.replace(" ", "_").upper()
            res = key+"(\""+chinese+"\"),\n\t\t\t" +\
                  key+"="+translate_result+"\n\t\t\t" +\
                  key+"="+chinese
            list.append(msg+res)
    if len(list) > 1:
        if not os.path.exists(resultFile):
            open(resultFile, 'w')
        file = open(resultFile, "a")
        for item in list:
            # print(item)
            file.write(item + "\n")


def matchChinese(string):
    flag = False
    chinese = ''
    # string = "aaaaa何时when 杖尔看see南雪snow，我me与梅花plum blossom两白头"
    res = re.findall('[\u4e00-\u9fa5]+.*[\u4e00-\u9fa5]+', string)
    if res:
        # print(str(res))
        flag = True
        chinese = res[0]
        res_2 = re.findall(r'[@*//]', string)
        if res_2:
            # print(res_2)
            flag = False
    return flag, chinese



if __name__ == "__main__":
    print("Hello Word!")
    # rootDir = "/Users/fby/IdeaProjects/noah/src/main/java/com/gitee/noah/"
    # dir = "service"
    # findFile(rootDir + dir)

    openFile("/Users/fby/PycharmProjects/HelloPython/find-chinese/test.txt")

