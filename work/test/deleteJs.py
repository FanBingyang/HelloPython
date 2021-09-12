# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  deleteJs.py    
@Desc   :  把程序员的自我修养中的html文件中引用的main.js给注释掉，能正常阅读不会跳转
@Author :  ByFan
@Time   :  2021/7/9 14:00 
'''
import os
import re

"""
    遍历指定路径下的htm文件，不迭代文件夹
"""
def ergodic(dirPath):
    for dir in os.listdir(dirPath):
        if dir.endswith('.htm'):
            print(dirPath + dir)
            annotation(dirPath + dir)

"""
    注释掉html文件中的包含main.js的script
"""
def annotation(filePath):
    with open(filePath,'r+',encoding='utf-8') as file:
        oldHtml = file.read()

    reStr = '.*main\.js.*'
    patern = re.compile(reStr)
    result = patern.findall(oldHtml)
    newStr = '<!-- ' + result[0] + ' -->'
    newHtml = re.sub(result[0],newStr,oldHtml)
    with open(filePath,'w',encoding='utf-8') as file:
        file.write(newHtml)


if __name__ == "__main__":
    ergodic('C:\\Users\\FBY\\Desktop\\阅读\\程序员的自我修养\\')
