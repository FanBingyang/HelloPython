# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  transform.py    
@Time   :  2020/5/25 19:04 
@Author :  ByFan
'''

import os

def transform(path="F:\\戏曲\\豫剧\\"):
    # 对输入的目录路径进行遍历
    for dir in os.listdir(path):
        # 判断当前是否是目录，是,那就进行递归遍历
        if os.path.isdir(path + "\\" + dir):
            transform(path + "\\" + dir)
        # 判断文件如果是以.exe结尾的，那么执行删除。
        elif dir.endswith('.rmvb'):
            portion = os.path.splitext(path+"\\"+dir)
            newname = portion[0]+'.MP4'
            os.rename(path+"\\"+dir,newname)
            print("转换格式:"+path+"\\"+dir)

if __name__=="__main__":
    transform()
