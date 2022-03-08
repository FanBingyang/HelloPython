# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  extractMySQL.py
@Desc   :  连接数据库导出创建表语句
@Author :  byfan
@Time   :  2021/12/9 10:06 
'''
import os
import pymysql


class DBTool:
    conn = None
    cursor = None
    host = None
    port = None
    user = None
    passwd = None
    db = None
    charset = 'utf-8'

    def __init__(self,mysqlConf):
        mysqlConf.toString()
        self.host = mysqlConf.host
        self.port = mysqlConf.port
        self.user = mysqlConf.user
        self.passwd = mysqlConf.password
        self.db = mysqlConf.database
        self.charset = mysqlConf.charset
        self.conn = pymysql.connect(host=self.host,
                                    port=self.port,
                                    user=self.user,
                                    passwd=self.passwd,
                                    db=self.db)
        self.cursor = self.conn.cursor()

    def execute_query(self, sql_string):
        try:
            cursor = self.cursor
            cursor.execute(sql_string)
            list = cursor.fetchall()
            cursor.close()
            self.conn.close()
            return list
        except pymysql.Error as e:
            print("mysql execute error:",e)
            raise

    # def execute_noquery(self, sql_string):
    #     try:
    #         cursor = self.cursor
    #         cursor.execute(sql_string)
    #         self.conn.commit()
    #         self.cursor.close()
    #         self.conn.close()
    #         return list
    #     except pymysql.Error as e:
    #         print("mysql execute error:",e)
    #         raise

    def exportMysql(self, sqlDir):
        # conn_dict = {
        #     'host': '121.41.199.102',
        #     'port': 3306,
        #     'user': 'root',
        #     'passwd': '123456',
        #     'database': 'picamass',
        #     'charset': 'utf8'
        # }
        # conn = DBTool(conn_dict)
        print("----------> 开始导出sql文件... <----------\n\n")
        # 查询所有数据库中所有表名
        sql_gettables = "select table_name from information_schema.`TABLES` WHERE TABLE_SCHEMA = '"+self.db+"';"
        list = self.execute_query(sql_gettables)

        # 文件目标路径，如果不存在，新建一个
        # mysql_file_path = '/Users/fby/Documents/testMysql'
        if not os.path.exists(sqlDir):
            os.mkdir(sqlDir)

        mysqldump_commad_dict = {'dumpcommad': 'mysqldump --no-data ', 'server': self.host, 'user': self.user,
                                 'password': self.passwd, 'port': self.port, 'db': self.db}

        if list:
            for row in list:
                # print(row[0])
                print("==> 开始导出", row[0] + ".sql...")
                # 切换到新建的文件夹中
                # os.chdir(mysql_file_path)
                # 表名
                dbtable = row[0]
                # 文件名
                exportfile = 'sql/'+row[0] + '.sql'
                # mysqldump 命令
                sqlfromat = "%s -h%s -u%s -p%s -P%s %s %s >%s"
                # 生成相应的sql语句
                sql = (sqlfromat % (mysqldump_commad_dict['dumpcommad'],
                                    mysqldump_commad_dict['server'],
                                    mysqldump_commad_dict['user'],
                                    mysqldump_commad_dict['password'],
                                    mysqldump_commad_dict['port'],
                                    mysqldump_commad_dict['db'],
                                    dbtable,
                                    exportfile))
                print('sql=',sql)
                result = os.system(sql)
                if result:
                    print("==>", row[0], ".sql 导出完成！！！\n")
                else:
                    print("==>", row[0], ".sql 导出失败！！！\n")
        print("----------> sql文件导出完成 <----------\n\n")

if __name__ == "__main__":
    print("Hello Word!")
    # DBTool.test(self="")
    # sql = "mysqldump --no-data  -h121.41.199.102 -uroot -p123456 -P3306 picamass >sql/picamass.sql"
    # os.system(sql)
    conn_dict = {
        'host': '121.41.199.102',
        'port': 3306,
        'user': 'root',
        'passwd': '123456',
        'db': 'picamass',
        'charset': 'utf8'
    }
    db = DBTool(conn_dict)
    print("1=", db.name)
    db.name = "hahaha"
    print("2=", db.name)
    print("3=", db)
