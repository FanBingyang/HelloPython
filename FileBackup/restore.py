# coding=utf-8
"""
    @Author：byFan
    @FileName： restore.py
    @Date：2023/7/21
    @Describe: 
"""
import os.path
import pstats


def openTar(rootPath, tarFileName, tarSuffix):
    tarFolderPath = os.path.join(rootPath, tarFileName)
    tarFile = tarFileName + "." + tarSuffix
    tarFilePath = os.path.join(rootPath, tarFile)
    cmdTemp = "tar -zxf %s -C %s"

    folderPathList = []
    if os.path.exists(tarFilePath):
        cmd = cmdTemp % (tarFilePath, rootPath)
        os.system(cmd)
        os.remove(tarFilePath)

        folderPathList.append(tarFolderPath)
        while folderPathList:
            for folderPath in folderPathList:
                for currentPath, dirs, files in os.walk(folderPath):
                    for file in files:
                        if file.endswith(tarSuffix):
                            print("file = ", file)
                            tarFilePath = os.path.join(currentPath, file)
                            print(tarFilePath)
                            cmd = cmdTemp % (tarFilePath, currentPath)
                            os.system(cmd)
                            os.remove(tarFilePath)

                for currentPath, dirs, files in os.walk(folderPath):
                    for dir in dirs:
                        folderPathList.append(os.path.join(currentPath, dir))
                folderPathList.remove(folderPath)


if __name__ == '__main__':
    print("Hello world!")
    root = "/Users/fby/PycharmProjects/HelloPython/CreatSpringBoot"
    tarFile = "FileBackup"
    tarSuffix = "bak.tgz"
    openTar(root, tarFile, tarSuffix)
