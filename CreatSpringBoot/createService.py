# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  createService.py    
@Desc   :  创建service层
@Author :  byfan
@Time   :  2021/12/9 22:39 
'''

import os
import time

from CreatSpringBoot import handleSql, FieldProperties

"""
返回格式化后的当前时间
"""
def getTime():
    timeFormat = "%Y/%m/%d %H:%M"
    return time.strftime(timeFormat, time.localtime())


"""
创建service
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test
@package: 所在包       eg：service
@entityName: 实体类名   eg:User
@entityIdType: 实体类主键类型  eg:Integer
"""
def writeService(projectPath, packageName, package, entityName, entityIdType):
    list = projectPath.split('/')
    projectName = list[len(list) - 1]
    projectExceptionName = projectName[-1:0].upper() + projectName[0:]
    packagePath = packageName.replace('.', '/')
    # entityName = entityName.title()
    fileName = entityName + "Service.java"
    print("==> 开始创建", fileName, "...")

    fullPath = projectPath + "/src/main/java/" + packagePath + "/" + package
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
    serviceFile = open(fullPath + "/" + fileName, "w", encoding="utf-8")
    # 写入包路径
    packageFull = "package " + packageName + "." + package + ";\n\n"
    serviceFile.write(packageFull)
    # 写入导包
    entity = entityName + "Entity"
    projectExption = projectExceptionName + "Exception"
    imports = ["import " + packageName + ".exception." + projectExption + ";\n",
               "import " + packageName + ".model." + entity + ";\n\n",
               "import java.util.List;\n\n"]
    serviceFile.writelines(imports)
    # 写入类注释
    notes = ["/**\n",
             " * @Description " + entityName + " Service层\n",
             " * @Author: byfan\n",
             " * @Date: " + getTime() + "\n",
             " */\n"]
    serviceFile.writelines(notes)
    clas = "public interface " + entityName + "Service {\n\n"
    serviceFile.write(clas)
    # 写入默认方法
    methods = ["\t/**\n",
               "\t * 新增/保存\n",
               "\t * @param " + entityName[0].lower() + entityName[1:] + "\n",
               "\t * @return \n",
               "\t * @throws " + projectExption + "\n",
               "\t */\n",
               "\t"+entity + " save(" + entity + " " + entityName[0].lower() + entityName[1:] + ") throws " + projectExption + ";\n\n",

               "\t/**\n",
               "\t * 根据id删除\n",
               "\t * @param id\n",
               "\t * @return \n",
               "\t * @throws " + projectExption + "\n",
               "\t */\n",
               "\tvoid deleteById("+entityIdType+" id) throws " + projectExption + ";\n\n",

               "\t/**\n",
               "\t * 查询全部\n",
               "\t * @return \n",
               "\t * @throws " + projectExption + "\n",
               "\t */\n",
               "\tList<"+entity+"> getAll() throws "+projectExption+";\n\n",

               "\t/**\n",
               "\t * 根据id查询\n",
               "\t * @param id\n",
               "\t * @return \n",
               "\t * @throws " + projectExption + "\n",
               "\t */\n",
               "\t"+entity+" getById("+entityIdType+" id) throws "+projectExption+";\n\n"
               ]
    serviceFile.writelines(methods)
    # 写入结尾括号
    serviceFile.write("}")
    print("==>", fileName, "创建完成！！！\n")

"""
创建serviceImpl
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test.service
@package: 所在包       eg：impl
@entityName: 实体类名   eg:User
@entityIdType: 实体类主键类型  eg:Integer
"""
def writeServiceImpl(projectPath, packageName, package, entityName, entityIdType):
    # entityName = entityName.title()
    list = projectPath.split('/')
    projectName = list[len(list) - 1]
    projectExceptionName = projectName[-1:0].upper() + projectName[0:]
    packagePath = packageName.replace('.', '/')
    fileName = entityName + "ServiceImpl.java"
    print("==> 开始创建", fileName, "...")

    fullPath = projectPath + "/src/main/java/" + packagePath + "/" + package
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
    serviceFile = open(fullPath + "/" + fileName, "w", encoding="utf-8")
    # 写入包路径
    packageFull = "package " + packageName + "." + package.replace('/', '.') + ";\n\n"
    serviceFile.write(packageFull)
    # 写入导包
    entity = entityName + "Entity"
    projectExption = projectExceptionName + "Exception"
    imports = ["import " + packageName + ".common.CommonResponse;\n",
               "import " + packageName + ".exception." + projectExption + ";\n",
               "import " + packageName + ".model." + entity + ";\n",
               "import " + packageName + ".dao." + entityName + "Dao;\n",
               "import " + packageName + ".service." + entityName + "Service;\n",
               "import lombok.extern.slf4j.Slf4j;\n",
               "import org.apache.commons.lang3.StringUtils;\n",
               "import org.springframework.beans.factory.annotation.Autowired;\n",
               "import org.springframework.stereotype.Service;\n\n"
               "import java.util.List;\n",
               "import java.util.Optional;\n\n"]
    serviceFile.writelines(imports)
    # 写入类注释
    notes = ["/**\n",
             " * @Description " + entityName + " ServiceImpl层\n",
             " * @Author: byfan\n",
             " * @Date: " + getTime() + "\n",
             " */\n"]
    serviceFile.writelines(notes)
    # 写入注解
    annotation = ["@Slf4j\n",
                  "@Service\n"]
    serviceFile.writelines(annotation)
    # 写入类名
    clas = "public class " + fileName[:fileName.find('.')] + " implements "+entityName+"Service {\n\n"
    serviceFile.write(clas)
    # 注入dao层
    serviceFile.write("\t@Autowired\n")
    daoName = entityName[0].lower()+entityName[1:]+"Dao"
    serviceFile.write("\tprivate "+ entityName+"Dao "+daoName+";\n\n")

    entityObjectName = entityName[0].lower() + entityName[1:]

    # 写入默认方法
    methods = ["\t/**\n",
               "\t * 新增/保存\n",
               "\t * @param " + entityName[0].lower()+entityName[1:] + "\n",
               "\t * @return \n",
               "\t * @throws " + projectExption + "\n",
               "\t */\n",
               "\t@Override\n",
               "\tpublic "+entity + " save(" + entity + " " + entityObjectName + ") throws " + projectExption + " {\n",
                "\t\treturn "+daoName+".save("+entityObjectName+");\n\t}\n\n",

               "\t/**\n",
               "\t * 根据id删除\n",
               "\t * @param id\n",
               "\t * @throws " + projectExption + "\n",
               "\t */\n",
               "\t@Override\n"
               "\tpublic void deleteById(" + entityIdType + " id) throws " + projectExption + "{\n",
               "\t\tif (id == null){\n",
               "\t\t\tlog.error(\"deleteById id is null!\");\n",
               "\t\t\tthrow new " + projectExption + "(CommonResponse.PARAM_ERROR,\"deleteById id is null!\");\n\t\t}\n",
               "\t\t" + daoName + ".deleteById(id);\n\t}\n\n",

               "\t/**\n",
               "\t * 查询全部\n",
               "\t * @return \n",
               "\t * @throws " + projectExption + "\n",
               "\t */\n",
               "\t@Override\n"
               "\tpublic List<"+entity+"> getAll() throws "+projectExption+" {\n",
               "\t\treturn "+daoName+".findAll();\n\t}\n\n",

               "\t/**\n",
               "\t * 根据id查询\n",
               "\t * @param id\n",
               "\t * @return \n",
               "\t * @throws " + projectExption + "\n",
               "\t */\n",
               "\t@Override\n"
               "\tpublic "+entity+" getById("+entityIdType+" id) throws "+projectExption+"{\n",
               "\t\tif (id == null){\n",
               "\t\t\tlog.error(\"getById id is null!\");\n",
               "\t\t\tthrow new "+projectExption+"(CommonResponse.PARAM_ERROR,\"getById id is null!\");\n\t\t}\n",
               "\t\tOptional<"+entity+"> optional = "+daoName+".findById(id);\n",
               "\t\treturn optional.orElse(null);\n\t}\n\n"
               ]
    serviceFile.writelines(methods)
    # 写入结尾括号
    serviceFile.write("}")
    print("==>", fileName, "创建完成！！！\n")


"""
service
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test
"""
def writeServiceAndImpl(projectPath,packageName,sqlFilePath):
    package = "service"
    print("\n----------> 开始创建 "+package+" 层 <----------")
    # 获取对象列表
    objectList = handleSql.getObjectList(sqlFilePath)
    # 循环创建service
    for object in objectList:
        sqlDesc = handleSql.getSqlDesc(object)
        writeService(projectPath, packageName, package, sqlDesc[0][FieldProperties.JavaField],sqlDesc[1][FieldProperties.JavaFieldType])
    print("----------> " + package + " 层创建完成 <----------\n")

    implPackage = "impl"
    print("\n----------> 开始创建 " + package + "." + implPackage + " 层 <----------")
    # 循环创建serviceImpl
    for object in objectList:
        sqlDesc = handleSql.getSqlDesc(object)
        writeServiceImpl(projectPath, packageName, package+"/"+implPackage, sqlDesc[0][FieldProperties.JavaField],
                     sqlDesc[1][FieldProperties.JavaFieldType])
    print("----------> " + package + "." + implPackage + " 层创建完成 <----------\n")




if __name__ == "__main__":
    print("Hello Word!")
    projectPath = "/Users/fby/PycharmProjects/HelloPython"
    packageName = "CreatSpringBoot"
    writeServiceAndImpl(projectPath, packageName)
