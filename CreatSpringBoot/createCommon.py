# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  createCommon.py
@Desc   :  创建common
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
创建CommonResponse.java
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test
@package: 所在包       eg：common
"""
def writeCommonResponse(projectPath, packageName, package):
    fileName = "CommonResponse.java"
    print("==> 开始创建", fileName, "...")

    packagePath = packageName.replace('.', '/')
    fullPath = projectPath + "/src/main/java/" + packagePath + "/" + package
    templateFile = "templateFiles/" + fileName
    oldFile = open(templateFile, "r" ,encoding="utf-8")
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
    newFile = open(fullPath + "/" + fileName, "w", encoding="utf-8")
    for line in oldFile.readlines():
        if "package com.byfan.springboottemplate" in line:
            line = "package "+ packageName +"."+package+";\n"
        if " * @Date:" in line:
            line = " * @Date: " + getTime() + "\n"
        newFile.write(line)
    print("==>", fileName, "创建完成！！！\n")


"""
创建ObjectResponse.java
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test
@package: 所在包       eg：common
"""
def writeObjectResponse(projectPath, packageName, package):
    fileName = "BaseResponse.java"
    print("==> 开始创建", fileName, "...")

    packagePath = packageName.replace('.','/')
    fullPath = projectPath + "/src/main/java/" + packagePath + "/" + package
    templateFile = "templateFiles/" + fileName
    oldFile = open(templateFile, "r" ,encoding="utf-8")
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
    newFile = open(fullPath + "/" + fileName,"w",encoding="utf-8")
    for line in oldFile.readlines():
        if "package com.byfan.springboottemplate" in line:
            line = "package "+ packageName + "."+package+";\n"
        if " * @Date:" in line:
            line = " * @Date: " + getTime() + "\n"
        newFile.write(line)
    print("==>", fileName, "创建完成！！！\n")


"""
创建ObjectResponse.java
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test
@package: 所在包       eg：common
"""
def writePageData(projectPath, packageName, package):
    fileName = "PageData.java"
    print("==> 开始创建", fileName, "...")

    packagePath = packageName.replace('.','/')
    fullPath = projectPath + "/src/main/java/" + packagePath + "/" + package
    templateFile = "templateFiles/" + fileName
    oldFile = open(templateFile, "r" ,encoding="utf-8")
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
    newFile = open(fullPath + "/" + fileName,"w",encoding="utf-8")
    for line in oldFile.readlines():
        if "package com.byfan.springboottemplate" in line:
            line = "package "+ packageName + "."+package+";\n"
        if " * @Date:" in line:
            line = " * @Date: " + getTime() + "\n"
        newFile.write(line)
    print("==>", fileName, "创建完成！！！\n")

"""
创建common层
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test
"""
def writeCommon(projectPath, packageName):
    package = "common"
    print("\n----------> 开始创建 " + package + " 层 <----------")
    # 创建CommonResponse.java
    writeCommonResponse(projectPath, packageName, package)
    # 创建ObjectResponse.java
    writeObjectResponse(projectPath, packageName, package)
    # 创建PageData.java
    writePageData(projectPath, packageName, package)
    print("----------> " + package + " 层创建完成 <----------\n")


if __name__ == "__main__":
    projectPath = "/Users/fby/PycharmProjects/HelloPython"
    packageName = "CreatSpringBoot"
    writeCommon(projectPath, packageName)