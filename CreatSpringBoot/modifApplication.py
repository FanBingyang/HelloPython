# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  modifApplication.py    
@Desc   :  
@Author :  byfan
@Time   :  2022/3/7 22:50 
'''

"""
修改Application
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
"""
def modifyApplication(projectPath, packagePath):
    list = projectPath.split('/')
    projectName = list[len(list) - 1]
    applicationName = projectName[-1:0].upper() + projectName[0:] + "Application.java"
    packagePath = packagePath.replace(".", "/")

    print("==> 开始创建", applicationName, "...")
    fullPath = projectPath + "/src/main/java/" + packagePath + "/" + applicationName

    applicationFile = open(fullPath, "r", encoding="utf-8")
    annotation = "@SpringBootApplication\n@EnableJpaAuditing\n@EnableScheduling"
    fileData = ""
    for line in applicationFile.readlines():
        if "@SpringBootApplication" in line:
            line = line.replace("@SpringBootApplication", annotation)
        fileData += line
    with open(fullPath, "w", encoding="utf-8") as f:
        f.write(fileData)


    print("==>", applicationName, "创建完成！！！\n\n")


if __name__ == "__main__":
    print("Hello Word!")
    projectPath = "/Users/fby/IdeaProjects/SpringBootTemplate"
    packageName = "com.byfan.springboottemplate"
    modifyApplication(projectPath,packageName)
