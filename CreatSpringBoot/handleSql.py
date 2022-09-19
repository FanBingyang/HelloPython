# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  handleSql.py    
@Desc   :  
@Author :  byfan
@Time   :  2021/12/10 15:35 
'''
import os
from CreatSpringBoot import FieldProperties

"""
将sql类型转换成自定义对应的java类型
"""
def sql2java(str):
    # mysql类型对应java字典
    dic = {
        "CHAR":"String",
        "VARCHAR":"String",
        "TINYBLOB":"String",
        "TINYTEXT":"String",
        "BLOB":"String",
        "TEXT":"String",
        "MEDIUMBLOB":"String",
        "MEDIUMTEXT":"String",
        "LONGBLOB":"String",
        "LONGTEXT":"String",
        "TINYINT":"Integer",
        "SMALLINT":"Integer",
        "MEDIUMINT":"Integer",
        "INT":"Integer",
        "INTEGER":"Integer",
        "BIGINT":"Integer",
        "FLOAT":"Float",
        "DOUBLE":"Double",
        "DATE":"Date",
        "TIME":"Date",
        "YEAR":"Date",
        "DATETIME":"Date",
        "TIMESTAMP":"Date",
    }
    # 将mysql类型转成大写，去字典取相应的值，如果没有对应关系默认返回String
    try:
        javaType = dic[str.upper()]
    except:
        javaType = "String"
    return javaType

"""
找到一个sql句中的字段名
"""
def findFieldName(str):
    # 通过截取获得``之间的字段内容
    start = str.find('`')
    end = str.rfind('`')
    return str[start+1 : end]


"""
找到一个sql语句中的注释
"""
def findNotes(str):
    # 通过截取获得''之间的注释内容
    start = str.find('\'')
    end = str.rfind('\'')
    # 没有注释默认返回空
    if start<0 or end<0:
        return ""
    return str[start+1 : end]


"""
将数据库字段转换成驼峰，生成类名
"""
def creatClassName(str):
    # 先将str每一段的首字母大写
    str = str.title()
    # 根据下划线将str分割成列表
    strList = str.split('_')
    # 再把列表拼成字符串
    className = "".join(strList)
    return className

"""
根据每一个建表语句生成字段名称
"""
def creatFieldName(str):
    # 先将数据库字段转换成驼峰
    fieldName = creatClassName(str)
    # 再将首字变为小写
    fieldName = fieldName[0].lower() + fieldName[1:]
    return fieldName

"""
从sql语句中获取字段类型
"""
def findFieldType(str):
    # 去除两端空格
    sqlStr = str.strip()
    # 通过空格分割成列表
    list = sqlStr.split(' ');
    # 取出sql字段类型
    sqlType = list[1]
    # 如果有字段长度，就把长度去掉
    start = sqlType.find('(')
    if start > 0:
        sqlType = sqlType[ : start]
    return sqlType

"""
查找主键字段，如果有多个，则以第一个为主
"""
def creatPrimaryKey(str,sqlDesc):
    start = str.find('(')
    end = str.find(')')
    str = str[start+1:end]
    list = str.split(',')       # eg:list = [`id`,`id2`]
    primarKey = list[0][1:-1]   # eg:primarKey = id
    for field in sqlDesc:
        if field[FieldProperties.SqlField]==primarKey:
            field[FieldProperties.PrimaryKey] = True
            break

"""
获取sql文件列表
@path sql文件夹路径 
"""
def getSqlFiles(path):
    sqlFileList = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == '.sql':
               sqlFileList.append(os.path.join(root,file))
    return sqlFileList


"""
从建表语句中提取表结构
@sqlFileName: sql文件路径
"""
def tableStructure(sqlFileName):
    # 读取建表的sql文件
    sqlFile = open(sqlFileName, 'r', encoding='utf-8')
    lines = sqlFile.readlines()
    # 存储表结构
    # 0：表名信息  1~n：字段信息
    sqlDesc = [{}]
    # 字段信息：0：sql字段、1：sql类型、2：sql注释、3：java字段、4：java类型        5：是否主键6：是否自增
    #           sqlField、sqlFieldType、fieldNotes、javaField、javaFieldType、AutoIncrement
    # 从每行sql中提取有效信息
    for line in lines:
        # 提取出表名等信息
        if (str(line).startswith("CREATE TABLE")):
            tableAttribute = {}
            tableAttribute[FieldProperties.SqlField] = findFieldName(line)
            tableAttribute[FieldProperties.SqlFieldType] = None
            tableAttribute[FieldProperties.FieldNotes] = None
            tableAttribute[FieldProperties.JavaField] = creatClassName(findFieldName(line))
            tableAttribute[FieldProperties.JavaFieldType] = None
            sqlDesc[0] = tableAttribute
        # 提取字段信息
        fieldAttribute = {}
        if str(line).strip().startswith("`"):
            fieldAttribute[FieldProperties.SqlField] = findFieldName(line)
            fieldAttribute[FieldProperties.SqlFieldType] = findFieldType(line)
            fieldAttribute[FieldProperties.FieldNotes] = findNotes(line)
            fieldAttribute[FieldProperties.JavaField] = creatFieldName(fieldAttribute[FieldProperties.SqlField])
            fieldAttribute[FieldProperties.JavaFieldType] = sql2java(fieldAttribute[FieldProperties.SqlFieldType])
            fieldAttribute[FieldProperties.PrimaryKey] = False
            fieldAttribute[FieldProperties.AutoIncrement] = False
            sqlDesc.append(fieldAttribute)
        if " AUTO_INCREMENT " in str(line).strip():
            fieldAttribute[FieldProperties.AutoIncrement] = True
        elif str(line).strip().startswith("PRIMARY KEY"):
            creatPrimaryKey(line,sqlDesc)
        elif str(line).strip().startswith(") ENGINE"):
            # 提取表注释
            sqlDesc[0][FieldProperties.FieldNotes] = findNotes(line)
            break
    return sqlDesc

""""
获取项目对象列表
"""
def getObjectList(path):
    objectList = []
    sqlFiles = getSqlFiles(path)
    for file in sqlFiles:
        start = file.find('/')
        end = file.find('.')
        fileName = file[start+1 : end].lower()
        objectList.append(fileName)
    return objectList

"""
通过objectName获取对象的sql结构
"""
def getSqlDesc(objectName):
    path = "sql"
    suffix = ".sql"
    objectName = objectName.lower()
    filePath = path + "/" + objectName + suffix
    sqlDesc = tableStructure(filePath)
    return sqlDesc

"""
删除sql文件夹下的临时sql文件
"""
def deleteSqlFiles(path):
    files = getSqlFiles(path)
    for file in files:
        os.remove(file)


if __name__ == "__main__":
    print("Hello Word!")
    deleteSqlFiles('sql')
