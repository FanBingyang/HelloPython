# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  modifPomXml.py    
@Desc   :  
@Author :  byfan
@Time   :  2021/12/13 14:03 
'''
import re

"""
从一行文件中提取出artifactId
"""
def getArtifactId(artifact):
    artifact = artifact.strip()
    pattern = re.compile('<artifactId>(.+)</artifactId>')
    result = pattern.findall(artifact)
    if result:
        return result[0]
    else:
        return ""


"""
创建application.yml
@projectPath: 项目路径  eg:/Users/xxx/IdeaProjects/test
"""
def updatePom(projectPath):
    pomImport = {
        "lombok": [
            "\t\t<!--lombok，编译时添加get/set方法-->\n",
            "\t\t<dependency>\n",
            "\t\t\t<groupId>org.projectlombok</groupId>\n",
            "\t\t\t<artifactId>lombok</artifactId>\n",
            "\t\t\t<version>1.18.10</version>\n",
            "\t\t\t<optional>true</optional>\n",
            "\t\t\t<scope>provided</scope>\n",
            "\t\t</dependency>\n"
        ],
        "mysql-connector-java": [
            "\t\t<!--引入mysql数据库依赖-->\n",
            "\t\t<dependency>\n",
            "\t\t\t<groupId>mysql</groupId>\n",
            "\t\t\t<artifactId>mysql-connector-java</artifactId>\n",
            "\t\t\t<version>8.0.18</version>\n",
            "\t\t</dependency>\n"
        ],
        "druid": [
            "\t\t<dependency>\n",
            "\t\t\t<groupId>com.alibaba</groupId>\n",
            "\t\t\t<artifactId>druid</artifactId>\n",
            "\t\t\t<version>1.1.12</version>\n",
            "\t\t</dependency>\n"
        ],
        "fastjson": [
            "\t\t<!--引入json依赖-->\n",
            "\t\t<dependency>\n",
            "\t\t\t<groupId>com.alibaba</groupId>\n",
            "\t\t\t<artifactId>fastjson</artifactId>\n",
            "\t\t\t<version>1.2.7</version>\n",
            "\t\t</dependency>\n"
        ],
        "knife4j-spring-boot-starter": [
            "\t\t<!-- Knife4j api文档 -->\n",
            "\t\t<dependency>\n",
            "\t\t\t<groupId>com.github.xiaoymin</groupId>\n",
            "\t\t\t<artifactId>knife4j-spring-boot-starter</artifactId>\n",
            "\t\t\t<version>2.0.7</version>\n"
            "\t\t</dependency>\n"
        ],
        "commons-lang3": [
            "\t\t<!-- 工具依赖 -->\n",
            "\t\t<dependency>\n",
            "\t\t\t<groupId>org.apache.commons</groupId>\n",
            "\t\t\t<artifactId>commons-lang3</artifactId>\n",
            "\t\t\t<version>3.10</version>\n",
            "\t\t</dependency>\n"],
        "commons-collections": [
            "\t\t<dependency>\n",
            "\t\t\t<groupId>commons-collections</groupId>\n",
            "\t\t\t<artifactId>commons-collections</artifactId>\n",
            "\t\t\t<version>3.2.2</version>\n",
            "\t\t</dependency>\n"
        ],
        "commons-io": [
            "\t\t<!--引入上传文件的依赖-->\n",
            "\t\t<dependency>\n",
            "\t\t\t<groupId>commons-io</groupId>\n",
            "\t\t\t<artifactId>commons-io</artifactId>\n",
            "\t\t\t<version>2.4</version>\n",
            "\t\t</dependency>\n"
        ],
        "commons-fileupload": [
            "\t\t<dependency>\n",
            "\t\t\t<groupId>commons-fileupload</groupId>\n",
            "\t\t\t<artifactId>commons-fileupload</artifactId>\n",
            "\t\t\t<version>1.3</version>\n",
            "\t\t</dependency>\n"
        ]
    }
    fileName = "pom.xml"
    print("==> 开始创建", fileName, "...")
    # 要额外引入的依赖
    # 最终的文件内容
    file_data = ""

    pomFile = open(projectPath + "/" + fileName, "r", encoding="utf-8")
    lines = pomFile.readlines()
    for line in lines:
        if "artifactId" in line:
            artifact_id = getArtifactId(line)
            # 提取artifact_id，如果额外依赖里有，则从额外依赖里剔除，避免重复引用
            if artifact_id in pomImport.keys():
                pomImport.pop(artifact_id)
        if "</dependencies>" in line:
            # 在引用最后，添加额外依赖
            for key in pomImport:
                for value in pomImport[key]:
                    file_data += value
        file_data += line
    # 将最终文件内容重新写入
    with open(projectPath + "/" + fileName, "w", encoding="utf-8") as f:
        f.write(file_data)

    print("==>", fileName, "创建完成！！！\n\n")


if __name__ == "__main__":
    print("Hello Word!")
    updatePom("/Users/fby/IdeaProjects/SpringBootTemplate")
