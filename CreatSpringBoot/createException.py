# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  createException.py    
@Desc   :  创建异常类
@Author :  byfan
@Time   :  2021/12/9 21:37 
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
创建GlobalExceptionHandler.java
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test
@package: 所在包       eg：exception
"""
def writeGlobalExceptionHandler(projectPath,packageName,package):
    fileName = "GlobalExceptionHandler.java"
    print("==> 开始创建", fileName, "...")

    list = projectPath.split('/')
    projectName = list[len(list) - 1]
    projectExceptionName = projectName[-1:0].upper() + projectName[0:]
    packagePath = packageName.replace('.', '/')
    fullPath = projectPath + "/src/main/java/" + packagePath + "/" + package

    templateFile = "templateFiles/" + fileName
    oldFile = open(templateFile, "r", encoding="utf-8-sig")

    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
    newFile = open(fullPath + "/" + fileName, "w", encoding="utf-8")
    for line in oldFile.readlines():
        if "com.byfan.springboottemplate" in line:
            line = line.replace("com.byfan.springboottemplate", packageName)
        if " * @Date:" in line:
            line = " * @Date: " + getTime() + "\n"
        if "SpringBootTemplateException" in line:
            line = line.replace("SpringBootTemplateException", projectExceptionName+"Exception")
        newFile.write(line)
    print("==>", fileName, "创建完成！！！\n")

"""
创建项目Exception.java
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test
@package: 所在包       eg：exception
"""
def writeProjectException(projectPath,packageName,package):
    list = projectPath.split('/')
    projectName = list[len(list) - 1]
    projectExceptionName = projectName[-1:0].upper() + projectName[0:]
    packagePath = packageName.replace('.','/')
    fileName = projectExceptionName+"Exception.java"
    print("==> 开始创建", fileName, "...")
    fullPath = projectPath + "/src/main/java/" + packagePath + "/" + package
    templateFile = "templateFiles/SpringBootTemplateException.java"
    oldFile = open(templateFile, "r", encoding="utf-8-sig")
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
    newFile = open(fullPath + "/" + fileName, "w", encoding="utf-8")
    for line in oldFile.readlines():
        if "com.byfan.springboottemplate" in line:
            line = line.replace("com.byfan.springboottemplate", packageName)
        if " * @Date:" in line:
            line = " * @Date: " + getTime() + "\n"
        if "SpringBootTemplateException" in line:
            line = line.replace("SpringBootTemplateException", projectExceptionName+"Exception")
        newFile.write(line)
    print("==>", fileName, "创建完成！！！\n")

"""
创建exception层
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test
"""
def writeExcept(projectPath,packageName):
    package = "exception"
    print("----------> 开始创建 "+package+" 层 <----------\n")
    # 创建GlobalExceptionHandler.java
    writeGlobalExceptionHandler(projectPath, packageName, package)
    # 创建项目Exception.java
    writeProjectException(projectPath, packageName, package)
    print("----------> " + package + " 层创建完成 <----------\n")

if __name__ == "__main__":
    projectPath = "/Users/fby/IdeaProjects/SpringBootTemplate"
    packageName = "com.byfan.springboottemplate"
    writeExcept(projectPath,packageName)