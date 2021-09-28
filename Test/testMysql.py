# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  testMysql.py    
@Time   :  2021/9/22 16:15 
@Author :  ByFan
'''
import pymysql

"""
测试数据库连接
"""
def testMysql():
    HOST = "127.0.0.1"
    PORT = 3306
    USER = "root"
    PASS_WORD = "123456"
    DB = "springboot_template"
    mysql = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASS_WORD, db=DB, charset="utf8")
    cursor = mysql.cursor()
    sql = "select * from user"
    cursor.execute(sql)
    # data = cursor.fetchone()
    # print(data)

    # 查询表的结构
    fields = cursor.description
    # print(fields)
    for i in fields:
        print(i)

if __name__ == '__main__':
    print("main")