# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  createKnife4jConfig.py
@Desc   :  创建swagger文档
@Author :  byfan
@Time   :  2021/12/9 16:12 
'''
import os
import time

"""
返回格式化后的当前时间
"""
def getTime():
    timeFormat = "%Y/%m/%d %H:%M"
    return time.strftime(timeFormat, time.localtime())


"""
创建Swagger2.java
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test
"""
def writeSwagger(projectPath,packageName):
    package = "config"
    list = projectPath.split('/')
    projectName = list[len(list) - 1][-1:0].upper() + list[len(list) - 1][0:]
    fileName = "Knife4jConfig.java"
    print("==> 开始创建", fileName, "...")
    packagePath = packageName.replace('.','/')
    fullPath = projectPath + "/src/main/java/" + packagePath + "/" + package
    templateFile = "templateFiles/" + fileName
    oldFile = open(templateFile, "r" ,encoding="utf-8")
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
    newFile = open(fullPath + "/" + fileName, "w", encoding="utf-8")
    for line in oldFile.readlines():
        if "package com.byfan.springboottemplate" in line:
            line = "package "+ packageName + "."+package+";\n"
        if " * @Date:" in line:
            line = " * @Date: " + getTime() + "\n"
        if "basePackage(\"com.byfan.springboottemplate.controller\")" in line:
            line = line.replace("com.byfan.springboottemplate",packageName)
        if "SpringBootTemplate项目接口文档" in line:
            line = line.replace("SpringBootTemplate",projectName)
        newFile.write(line)
    print("==>", fileName, "创建完成！！！\n")


if __name__ == "__main__":
    print("Hello Word!")
    projectPath = "/Users/fby/PycharmProjects/HelloPython"
    packageName = "CreatSpringBoot"
    writeSwagger(projectPath,packageName)
    print("-- end --")