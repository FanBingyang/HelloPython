# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  createDao.py    
@Desc   :  创建dao层
@Author :  byfan
@Time   :  2021/12/9 17:48 
'''

import os
import time

from CreatSpringBoot import FieldProperties
from CreatSpringBoot import handleSql

"""
返回格式化后的当前时间
"""
def getTime():
    timeFormat = "%Y/%m/%d %H:%M"
    return time.strftime(timeFormat, time.localtime())


"""
创建BaseRepository.java
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test
@package: 所在包       eg：dao
"""
def writeBaseRepository(projectPath, packageName, package):
    fileName = "BaseRepository.java"
    print("===> 开始创建", fileName, "...")
    packagePath = packageName.replace('.', '/')
    fullPath = projectPath + "/src/main/java/" + packagePath + "/" + package

    templateFile = "templateFiles/" + fileName
    oldFile = open(templateFile, "r", encoding="utf-8")
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
    newFile = open(fullPath + "/" + fileName, "w", encoding="utf-8")
    for line in oldFile.readlines():
        if "package com.byfan.springboottemplate" in line:
            line = "package " + packageName + "." + package + ";\n"
        if " * @Date:" in line:
            line = " * @Date: " + getTime() + "\n"
        newFile.write(line)
    print("===>", fileName, "创建完成！！！\n")


"""
创建实体类dao
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test
@package: 所在包       eg：dao
@entityName: 实体类名   eg:User
@entityIdType: 实体类主键类型  eg:Integer
"""
def writeEntityDao(projectPath, packageName, package, entityName, entityIdType):
    # entityName = entityName.title()
    entityIdType = entityIdType.title()
    fileName = entityName + "Dao.java"
    print("fileName == ", fileName)
    print("===> 开始创建", fileName, "...")
    packagePath = packageName.replace('.', '/')
    fullPath = projectPath + "/src/main/java/" + packagePath + "/" + package
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
    daoFile = open(fullPath + "/" + fileName, "w", encoding="utf-8")
    # 写入包路径
    packageFull = "package " + packageName + "." + package + ";\n\n"
    daoFile.write(packageFull)
    # 写入导包
    imports = ["import " + packageName + ".model." + entityName + "Entity;\n\n"]
    daoFile.writelines(imports)
    # 写入类注释
    notes = ["/**\n",
             " * @Description " + entityName + "持久层\n",
             " * @Author: byfan\n",
             " * @Date: " + getTime() + "\n",
             " */\n"]
    daoFile.writelines(notes)
    # 写入类名
    clas = 'public interface ' + entityName + 'Dao extends BaseRepository<' + entityName + 'Entity,' + entityIdType + '> {\n}\n'
    daoFile.write(clas)
    print("===>", fileName, "创建完成！！！\n")


"""
创建dao层
"""
def writeDao(projectPath, packageName, sqlFilePath):
    package = "dao"
    print("\n----------> 开始创建 " + package + " 层 <----------")
    writeBaseRepository(projectPath, packageName, package)
    # 获取对象列表
    objectList = handleSql.getObjectList(sqlFilePath)
    for object in objectList:
        sqlDesc = handleSql.getSqlDesc(object)
        writeEntityDao(projectPath, packageName, package, sqlDesc[0][FieldProperties.JavaField],sqlDesc[1][FieldProperties.JavaFieldType])

    print("----------> " + package + " 层创建完成 <----------\n")


if __name__ == "__main__":
    print("Hello Word!")
    projectPath = "/Users/fby/PycharmProjects/HelloPython"
    packageName = "CreatSpringBoot"
    writeDao(projectPath, packageName, "sql")
