# coding=utf-8
"""
    @Author：byFan
    @FileName： main.py
    @Date：2023/4/6
    @Describe: 
"""

import os

def listDir():
    root="/Users/fby/PycharmProjects/HelloPython/FileBackup"
    for root,dirs,files in os.walk(root):
        print("root = ",root)
        print("dirs = ",dirs)
        print("files = ",files)



if __name__ == '__main__':
    print("Hello world!")
    listDir()

# tar -cvjf jpg.tar.bz2 *.jpg