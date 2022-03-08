# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  mysqlConfigEntity.py
@Desc   :  
@Author :  byfan
@Time   :  2021/12/13 10:34 
'''

class mysqlConfig:
    'MySQL配置类'
    host = None
    port = 3306
    user = None
    passwd = None
    database = None
    charset = 'utf-8'

    # def __init__(self, mysqlconfig):
    #     self.host = mysqlconfig['MYSQL_HOST']
    #     self.port = mysqlconfig['MYSQL_PORT']
    #     self.user = mysqlconfig['MYSQL_USER']
    #     self.password = mysqlconfig['MYSQL_PWD']
    #     self.database = mysqlconfig['MYSQL_DATABASE']

    def __init__(self, host, port, user, password, database, charset='utf-8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset

    def getObject(self):
        config = {}
        config['host'] = self.host
        config['port'] = self.port
        config['user'] = self.user
        config['password'] = self.password
        config['database'] = self.database
        config['charset'] = self.charset
        return config

    def toString(self):
        object = self.getObject()
        print(object)


if __name__ == "__main__":
    print("Hello Word!")
    mc = mysqlConfig()
    mc.toString()
