# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  main.py    
@Desc   :  
@Author :  byfan
@Time   :  2021/12/13 15:20 
'''
import json

from CreatSpringBoot.extractMySQL import DBTool
from CreatSpringBoot.mysqlConfigEntity import mysqlConfig
import CreatSpringBoot.handleSql as handleSql
import CreatSpringBoot.extractMySQL as extractMySQL
import CreatSpringBoot.createController as createController
import CreatSpringBoot.createDao as createDao
import CreatSpringBoot.createException as createException
import CreatSpringBoot.createModel as createModel
import CreatSpringBoot.createService as createService
import CreatSpringBoot.createCommon as createCommon
import CreatSpringBoot.createKnife4jConfig as createKnife4jConfig
import CreatSpringBoot.createApplicationYml as createApplicationYml
import CreatSpringBoot.modifPomXml as modifPomXml
import CreatSpringBoot.modifApplication as modifApplication



if __name__ == "__main__":
    print("Hello Word!")
    # 1、输入项目信息
    # projectPath = input("输入项目路径：")
    # packageName = input("输入包名：")
    projectPath = "/Users/fby/IdeaProjects/SpringBootTemplate"
    packageName = "com.byfan.springboottemplate"

    # 2、读取数据库配置
    mysql_config_file_name = "config/mysql_config.json"
    mysql_config_file =  open(mysql_config_file_name, 'r', encoding="utf_8_sig")
    mysql_json_data = json.load(mysql_config_file)
    mysqlConf = mysqlConfig(mysql_json_data['MYSQL_HOST'], mysql_json_data['MYSQL_PORT'], mysql_json_data['MYSQL_USER'], mysql_json_data['MYSQL_PWD'], mysql_json_data['MYSQL_DATABASE'], mysql_json_data['MYSQL_CHARSET'])

    # 3、提取数据库表结构
    sqlDir = "sql"
    db = DBTool(mysqlConf)
    db.exportMysql(sqlDir)
    object_list = handleSql.getObjectList(sqlDir)
    # 4、创建model层
    createModel.writeModel(projectPath, packageName,sqlDir)
    # 5、创建dao层
    createDao.writeDao(projectPath, packageName,sqlDir)
    # 6、创建service层
    createService.writeServiceAndImpl(projectPath,packageName,sqlDir)
    # 7、创建controller层
    createController.writeController(projectPath, packageName,sqlDir)
    # 8、创建common层
    createCommon.writeCommon(projectPath, packageName)
    # 9、创建config/Knife4jConfig层
    createKnife4jConfig.writeSwagger(projectPath, packageName)
    # 10、创建exception层
    createException.writeExcept(projectPath, packageName)
    # 11、修改启动类Application
    modifApplication.modifyApplication(projectPath,packageName)
    # 13、创建application.yml
    createApplicationYml.writeApplicationYml(projectPath, mysqlConf)
    # 14、修改pom.xml
    modifPomXml.updatePom(projectPath)
    print("end")
    # handleSql.deleteSqlFiles(sqlDir)



