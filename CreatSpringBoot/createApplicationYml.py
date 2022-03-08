# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  createApplicationYml.py    
@Desc   :  创建配置文件
@Author :  byfan
@Time   :  2021/12/12 21:58 
'''
import os

"""
创建application.yml
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@mysqlConfig: MySQL配置类
"""
def writeApplicationYml(projectPath, mysqlConfig):
    list = projectPath.split('/')
    projectName = list[len(list) - 1].title()
    fileName = "application.yml"
    print("==> 开始创建", fileName, "...")
    fullPath = projectPath + "/src/main/resources/"
    templateFile = "templateFiles/" + fileName
    oldFile = open(templateFile, "r", encoding="utf-8")
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
    newFile = open(fullPath + "/" + fileName, "w", encoding="utf-8")
    for line in oldFile.readlines():
        if "MYSQL_HOST" in line:
            line = line.replace("MYSQL_HOST", mysqlConfig.host)
        if "MYSQL_PORT" in line:
            line = line.replace("MYSQL_PORT", str(mysqlConfig.port))
        if "MYSQL_DATABASE" in line:
            line = line.replace("MYSQL_DATABASE", mysqlConfig.database)
        if "MYSQL_USER" in line:
            line = line.replace("MYSQL_USER", mysqlConfig.user)
        if "MYSQL_PWD" in line:
            line = line.replace("MYSQL_PWD", mysqlConfig.password)
        if "MYSQL_CHARSET" in line:
            line = line.replace("MYSQL_CHARSET", mysqlConfig.charset)
        if "SpringBootTemplate" in line:
            line = line.replace("SpringBootTemplate", projectName)
        newFile.write(line)
    print("==>", fileName, "创建完成！！！\n\n")


if __name__ == "__main__":
    projectPath = "/Users/fby/PycharmProjects/HelloPython"
    print("Hello Word!")






