"""
针对U盘中病毒之后再文件下生成文件夹同名的.exe文件，遍历U盘删除.exe文件
"""
import os

def delete(path="I:\\"):
    # 对输入的目录路径进行遍历
    for dir in os.listdir(path):
        # 判断当前是否是目录，是,那就进行递归遍历
        if os.path.isdir(path + "\\" + dir):
            delete(path + "\\" + dir)
        # 判断文件如果是以.exe结尾的，那么执行删除。
        elif dir.endswith('.exe'):
            os.remove(path+"\\"+dir)
            print("删除:"+path+"\\"+dir)

if __name__=="__main__":
    delete()