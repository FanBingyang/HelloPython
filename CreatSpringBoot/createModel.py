# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  createModel.py
@Desc   :  创建实体类
@Author :  byfan
@Time   :  2021/9/18 16:10
'''
import os
import time
from CreatSpringBoot import FieldProperties
from CreatSpringBoot import handleSql



# *************************生成java文件操作*******************************************************

"""
返回格式化后的当前时间
"""
def getTime():
    timeFormat = "%Y/%m/%d %H:%M"
    return time.strftime(timeFormat, time.localtime())


"""
写入要导的基础包
"""
def writeImport(file,packName):
    # 写入package包路径
    package = "package "+packName+";\n\n"
    file.write(package)
    # 写入需要导入的包
    imports = ["import io.swagger.annotations.ApiModel;\n",
               "import io.swagger.annotations.ApiModelProperty;\n",
               "import lombok.Data;\n",
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
def writetClassName(file,fieldAttribute):
    fieldNotes = fieldAttribute[FieldProperties.FieldNotes]
    if fieldNotes == '':
        fieldNotes = fieldAttribute[FieldProperties.JavaField]
    # 写入类注释
    notes = ["/**\n",
             " * @Description " + fieldNotes + "实体类\n",
             " * @Author: byfan\n",
             " * @Date: " + getTime() + "\n",
             " */\n"]
    file.writelines(notes)
    # 写入类注解
    annotation = ["@ApiModel(value = \"" + fieldNotes + "实体类\", description = \"" + fieldNotes +"Entity\")\n",
                  "@EntityListeners(AuditingEntityListener.class)\n",
                  "@Entity\n",
                  "@Data\n"]
    file.writelines(annotation)
    # 写入表映射
    table = '@Table(name = "'+ fieldAttribute[FieldProperties.SqlField] +'")\n'
    file.write(table)
    # 写入类名
    clas = 'public class '+ fieldAttribute[FieldProperties.JavaField] +'Entity implements Serializable {\n\n'
    file.write(clas)

"""
写入类字段属性
@fields 
"""
def writeField(file,fields):
    for fieldAttribute in fields:
        # 写入字段注释
        notes = ["\t/**\n",
                 "\t * "+ fieldAttribute[FieldProperties.FieldNotes] +"\n",
                 "\t */\n"]
        file.writelines(notes)

        file.write("\t@ApiModelProperty(value = \""+ fieldAttribute[FieldProperties.FieldNotes] +"\")\n")

        # 有四种特殊情况需要额外加注释，分别是主键、是否自增、创建时间和修改时间
        if fieldAttribute[FieldProperties.PrimaryKey]:
            file.write('\t@Id\n')
        if fieldAttribute[FieldProperties.AutoIncrement]:
            file.write('\t@GeneratedValue(strategy = GenerationType.IDENTITY)\n')
        if fieldAttribute[FieldProperties.SqlField] == 'create_time':
            file.write('\t@CreatedDate\n')
        elif fieldAttribute[FieldProperties.SqlField] == 'update_time':
            file.write('\t@LastModifiedDate\n')

        # 写入表映射
        tableField = '\t@Column(name = "'+ fieldAttribute[FieldProperties.SqlField] +'")\n'
        file.write(tableField)

        # 写入属性字段
        javaField = "\tprivate "+ fieldAttribute[FieldProperties.JavaFieldType] +" " + fieldAttribute[FieldProperties.JavaField] +";\n\n"
        file.write(javaField)

"""
创建实体类
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test
@package: 所在包       eg：model
@sqlDesc              eg：sql结构
"""
def writeEntity(projectPath, packageName, package, sqlDesc):
    fileName = sqlDesc[0][FieldProperties.JavaField] + 'Entity.java'
    print("==> 开始创建"+fileName+"实体类...")
    packagePath = packageName.replace('.', '/')
    fullPath = projectPath + "/src/main/java/" + packagePath + "/" + package

    # 判断文件夹是否存在
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
    # 创建文件
    file = open(fullPath + "/" + fileName, 'w+', encoding='utf-8')

    # 写入需要导入的包
    writeImport(file, packageName + "." + package)
    # 写入类注解和类名
    writetClassName(file, sqlDesc[0])

    # 遍历表结构，写入类属性字段
    writeField(file, sqlDesc[1:])

    # 写入结尾大括号
    file.write("}")
    print("==>", fileName, "实体类创建完成！！！\n")


"""
创建model层实体类
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test
"""
def writeModel(projectPath, packageName, sqlFilePath):
    package = "model"
    print("\n----------> 开始创建 "+package+" 层 <----------")
    # 获取对象列表
    objectList = handleSql.getObjectList(sqlFilePath)
    # 循环创建实体类
    for object in objectList:
        sqlDesc = handleSql.getSqlDesc(object)
        writeEntity(projectPath,packageName,package,sqlDesc)

    print("----------> "+package+" 层创建完成 <----------\n")

# ********************************main方法************************************************************
if __name__ == '__main__':
    projectPath = "/Users/fby/PycharmProjects/HelloPython"
    packageName = "CreatSpringBoot"
    writeModel(projectPath,packageName)






