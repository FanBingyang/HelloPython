# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  MyException.py    
@Time   :  2021/9/24 10:29 
@Author :  ByFan
'''

class MyException(Exception):
    def __init__(self,err='MyExceptionErr'):
        self.err = err
        Exception.__init__(self,err)

    def __str__(self):
        print(self.err)

if __name__ == '__main__':
    print("Hello python!")
    try:
        try:
            # raise MyException('aaaa')
            i = 1/0
        except Exception as e:
            print("捕获异常")
            print("异常信息为：",e)
            raise MyException('aaa')
    except MyException as me:
        print("me===",me)