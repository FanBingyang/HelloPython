# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  createController.py    
@Desc   :  创建controller层
@Author :  byfan
@Time   :  2021/12/10 17:42 
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
创建实体类
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test
@package: 所在包       eg：controller
@sqlDesc              eg：sql结构
"""
def writeEntityController(projectPath, packageName, package, sqlDesc):
    entityName = sqlDesc[0][FieldProperties.JavaField]
    classNote = sqlDesc[0][FieldProperties.FieldNotes][:-1]
    if classNote == '':
        classNote = entityName
    print("classNote="+classNote)
    fileName = entityName + "Controller.java"
    print("==> 开始创建" + fileName + "...")

    list = projectPath.split('/')
    projectName = list[len(list) - 1]
    projectExceptionName = projectName[-1:0].upper() + projectName[0:]
    packagePath = packageName.replace('.', '/')

    fullPath = projectPath + "/src/main/java/" + packagePath + "/" + package
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)

    controllerFile = open(fullPath + "/" + fileName, "w", encoding="utf-8")
    # 写入包路径
    packageFull = "package " + packageName + "." + package + ";\n\n"
    controllerFile.write(packageFull)
    # 写入导包
    entity = entityName + "Entity"
    service = entityName + "Service"
    projectExption = projectExceptionName + "Exception"
    imports = ["import " + packageName + ".common.CommonResponse;\n",
               "import " + packageName + ".common.BaseResponse;\n",
               "import " + packageName + ".exception."+projectExption+";\n",
               "import " + packageName + ".model."+entity+";\n",
               "import " + packageName + ".service."+service+";\n",
               "import io.swagger.annotations.Api;\n",
               "import io.swagger.annotations.ApiOperation;\n",
               "import lombok.extern.slf4j.Slf4j;\n",
               "import org.springframework.beans.factory.annotation.Autowired;\n",
               "import org.springframework.web.bind.annotation.RequestMapping;\n",
               "import org.springframework.web.bind.annotation.RequestMethod;\n",
               "import org.springframework.web.bind.annotation.RestController;\n\n",
               "import java.util.List;\n\n"]
    controllerFile.writelines(imports)
    # 写入类注释
    notes = ["/**\n",
             " * @Description " + classNote + "控制层\n",
             " * @Author: byfan\n",
             " * @Date: " + getTime() + "\n",
             " */\n"]
    controllerFile.writelines(notes)
    # 写入注解
    annotation = ["@Slf4j\n",
                  "@Api(tags = \""+classNote+"接口\")\n",
                  "@RestController\n",
                  "@RequestMapping(\"/api/"+entityName.lower()+"\")\n"]
    controllerFile.writelines(annotation)
    # 写入类名
    clas = "public class " + fileName[:fileName.find('.')] + " {\n\n"
    controllerFile.write(clas)
    # 注入service层
    controllerFile.write("\t@Autowired\n")
    controllerFile.write("\tprivate " + service + " " +service[0].lower()+service[1:] + ";\n\n")
    # 写入默认方法
    methods = ["\t/**\n",
               "\t * 新增/修改\n",
               "\t * @param " + entityName[0].lower() + entityName[1:] + "\n",
               "\t * @return \n",
               "\t */\n",
               "\t@ApiOperation(\"新增/修改"+classNote+"信息\")\n",
               "\t@RequestMapping(value = \"/save\",method = RequestMethod.POST)\n",
               "\tpublic BaseResponse<"+entity+"> save(" + entity + " " + entityName[0].lower()+entityName[1:] + ") {\n",
               "\t\tBaseResponse<"+entity+"> response = new BaseResponse();\n",
               "\t\ttry {\n",
               "\t\t\t"+entity+" "+entityName[0].lower()+" = "+service[0].lower()+service[1:]+".save("+entityName[0].lower()+entityName[1:]+");\n",
               "\t\t\tresponse.setData("+entityName[0].lower()+");\n",
               "\t\t\tresponse.setCode(CommonResponse.OK.code);\n",
               "\t\t\treturn response;\n",
               "\t\t} catch ("+projectExption+" e) {\n",
               "\t\t\tlog.error(\"save is except ,e: \", e);\n",
               "\t\t\tresponse.setCode(e.getErrorCode());\n",
               "\t\t\tresponse.setMsg(e.getMessage());\n",
               "\t\t\treturn response;\n",
               "\t\t}\n",
               "\t}\n\n",

               "\t/**\n",
               "\t * 根据id删除" + classNote + "信息\n",
               "\t * @param id\n",
               "\t * @return \n",
               "\t */\n",
               "\t@ApiOperation(\"根据id删除" + classNote + "信息\")\n",
               "\t@RequestMapping(value = \"/deleteById\",method = RequestMethod.DELETE)\n",
               "\tpublic BaseResponse<Void> deleteById(" + sqlDesc[1][FieldProperties.JavaFieldType] + " id) {\n",
               "\t\tBaseResponse<Void> response = new BaseResponse();\n",
               "\t\ttry {\n",
               "\t\t\t" + service[0].lower() + service[1:] + ".deleteById(id);\n",
               "\t\t\tresponse.setCode(CommonResponse.OK.code);\n",
               "\t\t\treturn response;\n",
               "\t\t} catch (" + projectExption + " e) {\n",
               "\t\t\tlog.error(\"deleteById is except ,e: \", e);\n",
               "\t\t\tresponse.setCode(e.getErrorCode());\n",
               "\t\t\tresponse.setMsg(e.getMessage());\n",
               "\t\t\treturn response;\n",
               "\t\t}\n",
               "\t}\n\n",


               "\t/**\n",
               "\t * 查询全部\n",
               "\t * @return \n",
               "\t */\n",
               "\t@ApiOperation(\"查询全部"+classNote+"信息\")\n",
               "\t@RequestMapping(value = \"/getAll\",method = RequestMethod.GET)\n",
               "\tpublic BaseResponse<List<"+entity+">> getAll() {\n",
               "\t\tBaseResponse<List<"+entity+">> response = new BaseResponse();\n",
               "\t\ttry {\n",
               "\t\t\tList<"+entity+"> all = "+service[0].lower()+service[1:]+".getAll();\n",
               "\t\t\tresponse.setData(all);\n",
               "\t\t\tresponse.setCode(CommonResponse.OK.code);\n",
               "\t\t\treturn response;\n",
               "\t\t} catch ("+projectExption+" e) {\n",
               "\t\t\tlog.error(\"getAll is except ,e: \", e);\n",
               "\t\t\tresponse.setCode(e.getErrorCode());\n",
               "\t\t\tresponse.setMsg(e.getMessage());\n",
               "\t\t\treturn response;\n",
               "\t\t}\n",
               "\t}\n\n",

               "\t/**\n",
               "\t * 根据id查询"+classNote+"信息\n",
               "\t * @param id\n",
               "\t * @return \n",
               "\t */\n",
               "\t@ApiOperation(\"根据id查询" + classNote + "信息\")\n",
               "\t@RequestMapping(value = \"/getById\",method = RequestMethod.GET)\n",
               "\tpublic BaseResponse<"+entity+"> getById("+sqlDesc[1][FieldProperties.JavaFieldType]+" id) {\n",
               "\t\tBaseResponse<"+entity+"> response = new BaseResponse();\n",
               "\t\ttry {\n",
               "\t\t\t" + entity + " "+ entityName.lower() +" = " + service[0].lower()+service[1:] + ".getById(id);\n",
               "\t\t\tresponse.setData("+entityName.lower()+");\n",
               "\t\t\tresponse.setCode(CommonResponse.OK.code);\n",
               "\t\t\treturn response;\n",
               "\t\t} catch (" + projectExption + " e) {\n",
               "\t\t\tlog.error(\"getById is except ,e: \", e);\n",
               "\t\t\tresponse.setCode(e.getErrorCode());\n",
               "\t\t\tresponse.setMsg(e.getMessage());\n",
               "\t\t\treturn response;\n",
               "\t\t}\n",
               "\t}\n\n"
               ]
    controllerFile.writelines(methods)
    # 写入结尾括号
    controllerFile.write("}")

    print("==>", fileName, "创建完成！！！\n")

"""
创建controller层
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
@packageName: 包名     eg:com.byfan.test
"""
def writeController(projectPath,packageName,sqlFilePath):
    package = "controller"
    print("\n----------> 开始创建 "+package+" 层 <----------")
    # 获取对象列表
    objectList = handleSql.getObjectList(sqlFilePath)
    # 循环创建实体类
    for object in objectList:
        sqlDesc = handleSql.getSqlDesc(object)
        writeEntityController(projectPath, packageName, package, sqlDesc)

    print("----------> " + package + " 层创建完成 <----------\n")


if __name__ == "__main__":
    print("Hello Word!")
    projectPath = "/Users/fby/PycharmProjects/HelloPython"
    packageName = "CreatSpringBoot"
    writeController(projectPath, packageName)