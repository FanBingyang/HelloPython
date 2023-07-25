# coding=utf-8
"""
    @Author：byFan
    @FileName： backUp.py
    @Date：2023/4/6
    @Describe: 
"""

import os
import shutil



def deletTarExcludeFiles(rootPath, folder, tarExcludeFile):
    """
    删除根据层级打包规则所产生的打包过滤文件
    @param rootPath:
    @param folder
    @param tarExcludeFile:
    @return:
    """
    rootFullPath = os.path.join(rootPath, folder)
    for currentPath, dirs, files in os.walk(rootFullPath, topdown=False):
        if tarExcludeFile in files:
            os.remove(os.path.join(currentPath, tarExcludeFile))
            print("已经删除：", os.path.join(currentPath, tarExcludeFile))


def deletTarFiles(rootPath, folder, tarSuffix):
    """
    删除根据层级打包规则所产生的打包文件
    @param rootPath:
    @param folder:
    @param tarSuffix:
    @return:
    """
    rootFullPath = os.path.join(rootPath, folder)
    for currentPath, dirs, files in os.walk(rootFullPath, topdown=False):
        for dir in dirs:
            os.remove(os.path.join(currentPath, dir+"."+tarSuffix))
            print("已经删除：", os.path.join(currentPath, dir+"."+tarSuffix))
    folderTar = os.path.join(rootPath, folder + "." + tarSuffix)
    if os.path.exists(folderTar):
        os.remove(folderTar)
        print("已经删除：", folderTar)


def createTar(rootPath, folder, tarSuffix):
    """
    根据层级打包规则，将指定路径 rootPath 下 folder 文件夹进行打包，打包文件后缀为 tarSuffix
    层级打包规则：将指定文件夹下的子文件夹，依次打包。针对文件夹每次打包时都排出子文件夹，而将子文件夹的打包文件进行打包进去。
    @param rootPath: 文件夹所在路径
    @param folder: 要操作的文件夹
    @param tarSuffix: 打包后缀
    @return:
    """
    rootFullPath = os.path.join(root, folder)
    cmdExclude = "tar -zcf %s.%s -X %s/%s -C %s ./%s"
    cmdAll = "tar -zcf %s.%s -C %s ./%s"
    for currentPath, dirs, files in os.walk(rootFullPath, topdown=False):
        print("currentPath = ", currentPath)
        print("files = ", files)
        if dirs:
            with open(os.path.join(currentPath, tarExcludeFile), 'w') as f:
                f.write(tarExcludeFile + "\n")
                for dir in dirs:
                    operaFolderPath = os.path.join(currentPath, dir)
                    print("dir : ", operaFolderPath)
                    f.write(dir + "\n")
                    cmd = cmdExclude % (operaFolderPath, tarSuffix, operaFolderPath, tarExcludeFile, currentPath, dir)
                    for rt, ds, fs in os.walk(operaFolderPath):
                        if len(ds) == 0:
                            cmd = cmdAll % (operaFolderPath, tarSuffix, currentPath, dir)
                            break
                        else:
                            break
                    print("cmd", cmd)
                    os.system(cmd)
        print("------------------------")
    if os.path.exists(tarExcludeFile):
        cmd = cmdExclude % (rootFullPath, tarSuffix, rootFullPath, tarExcludeFile, rootPath, folder)
    else:
        cmd = cmdAll % (rootFullPath, tarExcludeFile, rootPath, folder)
    print("==> cmd", cmd)
    os.system(cmd)


def copyTar(sourceTar, targetPath):
    if os.path.exists(sourceTar):
        shutil.copy(sourceTar, targetPath)
        print("已经将源文件 %s 复制到目标路径下 %s" % (sourceTar, targetPath))
    else:
        print("源文件不存在")



if __name__ == '__main__':
    print("Hello world!")
    root = "/Users/fby/PycharmProjects/HelloPython"
    folder = "FileBackup"
    targetPath = "/Users/fby/PycharmProjects/HelloPython/CreatSpringBoot"
    fullPath = os.path.join(root, folder)
    tarExcludeFile = "tar.exclude.list"
    tarSuffix = "bak.tgz"

    createTar(root, folder, tarSuffix)
    copyTar(fullPath + "." + tarSuffix, targetPath)
    deletTarExcludeFiles(root, folder, tarExcludeFile)
    deletTarFiles(root, folder, tarSuffix)
