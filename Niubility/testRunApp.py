import os
import winreg
import ctypes

# print("打开QQ音乐")
# os.system("E:\\Tencent\\qqmusic\\QQMusic.exe")

# os.system("E:\\网易邮箱\\MailMaster\\Application\\mailmaster.exe")

# os.startfile("C:\\Users\\FBY\Desktop\QQ.lnk")

# def get_desktop():
#     key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
#                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
#     print(winreg.QueryValueEx(key,"Desktop")[0])

#
# def get_desk_p():
#     return os.path.join(os.path.expanduser('~'),"Desktop")
# #
# if __name__=="__main__":
#     # print(get_desk_p())
#     # get_desktop()
#
#     path = get_desk_p()
#     # 对输入的目录路径进行遍历
#     for dir in os.listdir(path):
#         # 判断当前是否是目录，是,那就进行递归遍历
#         if os.path.isdir(path + "\\" + dir):
#             # delete(path + "\\" + dir)
#             print("文件夹：" + path+"\\"+dir)
#         # 判断文件如果是以.exe结尾的，那么执行删除。
#         else:
#             print("文件：" + path + "\\" + dir)

    # os.startfile('C:\\Users\\FBY\\Desktop\\QQ.lnk')

# s = "打开QQ音乐"
# print(s.find("打开"))
# s=s[2:]
# print(s)


# lpBuffer = ctypes.create_string_buffer(78)
# ctypes.windll.kernel32.GetLogicalDriveStringsA(ctypes.sizeof(lpBuffer), lpBuffer)
# vol = lpBuffer.raw.split("\x00")
# for i in vol:
#     print(i)
#
def findPath(path,appName):
    try:
        # 对输入的目录路径进行遍历
        for dir in os.listdir(path):
            # 判断当前是否是目录，是,那就进行递归遍历
            if os.path.isdir(path + "\\" + dir):
                findPath(path + "\\" + dir,appName)
            elif appName == dir:
                # print(path + "\\" + dir)
                return path + "\\" + dir
    except:
        # print("无法访问")
        pass


# 遍历字母A到Z，忽略光驱的盘符
# volList = []
# for i in range(65, 91):
#     vol = chr(i) + ':'
#     if os.path.isdir(vol):
#         volList.append(vol)
# print("vol=",volList)
#
# for path in volList:
#     find(path)



# for k,v in appName_List.items():
#     for i,j in v.items():
#         print("key_1:",k,"    key_2:",i,"    value:",j)

# 遍历字母A到Z，忽略光驱的盘符
volList = []
for i in range(65, 91):
    vol = chr(i) + ':'
    if os.path.isdir(vol):
        volList.append(vol)

# for k,v in appName_List.items():
#     for i,j in v.items():
#         for vol in volList:
            # appName_List[k][i] = findPath(vol,i)
            # print(findPath(vol,'MicrosoftEdge.exe'))
# for k,v in appName_List.items():
#     for i,j in v.items():
#         print("key_1:",k,"    key_2:",i,"    value:",j)

os.startfile('E:Google\\Chrome\\Application\\chrome.exe')

