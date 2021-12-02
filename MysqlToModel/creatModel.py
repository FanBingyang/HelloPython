# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  creatModel.py
@Time   :  2021/9/18 16:10 
@Author :  ByFan
'''


# ***********************************从建表sql语句中提取相关信息操作******************************************************

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
从建表语句中提取表结构
"""
def tableStructure():
    # 读取建表的sql文件
    sqlFile = open('table.sql', 'r', encoding='utf-8')
    lines = sqlFile.readlines()
    # 存储表结构
    # 0：sql字段、1：sql类型、2：sql注释、3：java字段、4：java类型
    sqlDesc = [[]]

    # 提取出表名等信息
    sqlDesc[0] = [findFieldName(lines[0]), None, findNotes(lines[len(lines) - 1]), creatClassName(findFieldName(lines[0])), None]

    # 提取字段信息
    for i in range(1, len(lines) - 2):
        line = lines[i]
        list = []
        list.append(findFieldName(line))
        list.append(findFieldType(line))
        list.append(findNotes(line))
        list.append(creatFieldName(list[0]))
        list.append(sql2java(list[1]))
        sqlDesc.append(list)
    return sqlDesc


# *************************生成java文件操作*******************************************************
"""
写入要导的基础包
"""
def writeImport(file):
    # 写入package包路径
    package = "package com.baidu.ide.model;\n\n"
    file.write(package)
    # 写入需要导入的包
    imports = ["import lombok.Data;\n",
               "import org.springframework.data.annotation.CreatedDate;\n",
               "import org.springframework.data.annotation.LastModifiedDate;\n",
               "import org.springframework.data.jpa.domain.support.AuditingEntityListener;\n\n",
               "import javax.persistence.*;\n",
               "import java.io.Serializable;\n",
               "import java.util.Date;\n\n"]
    file.writelines(imports)

"""
写入类名和表映射
"""
def writetClassName(file,list):
    # 写入类注释
    notes = ["/**\n",
             " * " + list[2] + "实体类\n",
             " */\n"]
    file.writelines(notes)
    # 写入类注解
    annotation = ["@Entity\n",
               "@EntityListeners(AuditingEntityListener.class)\n",
               "@Data\n",]
    file.writelines(annotation)
    # 写入表映射
    table = '@Table(name = "'+ list[0] +'")\n'
    file.write(table)
    # 写入类名
    clas = 'public class '+ list[3] +'Entity implements Serializable {\n\n'
    file.write(clas)

"""
写入类属性
"""
def writeField(file,list):
    # 写入字段注释
    notes = ["\t/**\n",
             "\t * "+ list[2] +"\n",
             "\t */\n"]
    file.writelines(notes)

    # 有三种特殊情况需要额外加注释，分别是主键、创建时间和修改时间
    if list[0] == 'id':
        file.write('\t@Id\n')
        file.write('\t@GeneratedValue(strategy = GenerationType.IDENTITY)\n')
    elif list[0] == 'create_time':
        file.write('\t@CreatedDate\n')
    elif list[0] == 'update_time':
        file.write('\t@LastModifiedDate\n')

    # 写入表映射
    tableField = '\t@Column(name = "'+ list[0] +'")\n'
    file.write(tableField)

    # 写入属性字段
    javaField = '\tprivate '+ list[4] +' ' + list[3] +';\n\n'
    file.write(javaField)


# ********************************main方法************************************************************
if __name__ == '__main__':
    print("开始创建实体类......\n")

    # 提取数据库表结构
    sqlDesc = tableStructure()

    # 创建文件
    file =  open(sqlDesc[0][3]+'Entity.java', 'w+', encoding='utf-8')

    # 写入需要导入的包
    writeImport(file)
    # 写入类注解和类名
    writetClassName(file,sqlDesc[0])
    # 遍历表结构，写入类属性字段
    for i in range(1,len(sqlDesc)):
        writeField(file,sqlDesc[i])
    # 写入结尾大括号
    file.write("}")

    print("实体类创建完成！！！")





