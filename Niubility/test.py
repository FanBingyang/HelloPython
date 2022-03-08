import os
import webbrowser
from Niubility import Baymax
# volList = []
# for i in range(65, 91):
#     vol = chr(i) + ':'
#     if os.path.isdir(vol):
#         volList.append(vol)
# print("vol=",volList)

"""
QQ.exe
TIM.exe
WeChat.exe
QQMusic.exe
QQLive.exe
QyClient.exe
chrome.exe
firefox.exe
"""

appName_List = {'QQ':'QQ.exe','TIM':'TIM.exe','微信':'WeChat.exe',
                'QQ音乐':'QQMusic.exe','网易音乐':'cloudmusic.exe',
                '腾讯视频': 'QQLive.exe','爱奇艺': 'QyClient.exe',
                '谷歌浏览器': 'chrome.exe','火狐浏览器': 'firefox.exe'}
appPath_List = {'QQ.exe':'','TIM.exe':'','WeChat.exe':'',
                'QQMusic.exe':'','cloudmusic.exe':'',
                'QQLive.exe':'','QyClient.exe':'',
                'chrome.exe':'','firefox.exe':''}

appName_List = {'QQ': {'QQ.exe':'1'},
                'TIM': {'TIM.exe':'2'},
                '微信': {'WeChat.exe':'3'},
                'QQ音乐': {'QQMusic.exe':'4'},
                '腾讯视频': {'QQLive.exe':'5'},
                '爱奇艺': {'QyClient.exe':'6'},
                '谷歌浏览器': {'chrome.exe':'7'},
                '火狐浏览器': {'firefox.exe':'8'}}

"""查找指定软件的执行文件路径"""
# def findPath(path,appName):
#     try:
#         # 对输入的目录路径进行遍历
#         for dir in os.listdir(path):
#             # 判断当前是否是目录，是,那就进行递归遍历
#             if os.path.isdir(path + "\\" + dir):
#                 # print(path + "\\" + dir)
#                 findPath(path + "\\" + dir, appName)
#             elif appName == dir:
#                 print(path + "\\" + dir)
#                 appPath = path + "\\" + dir
#                 print("apPath:",appPath)
#                 return appPath
#     except:
#         pass

# def findPath_2(path,appName):
#     for root, dirs, files in os.walk(path):
#         if appName in dirs or appName in files:
#             print("root:",root,"\t",type(root))
#             # root = str(root)
#             return os.path.join(root, appName)
#     else:
#         return False

# volList = []
# for i in range(65, 91):
#     vol = chr(i) + ':'
#     if os.path.isdir(vol):
#         volList.append(vol)
# print("volList=",volList)
# app = 'chrome.exe'
# findPath("C:",app)
# print("path=====",)
# for vol in volList:
#     print("path=====",findPath(vol,app))
    # print("path= ",path)
    # if path != '' or path != 'None':
    #     print(vol,"\t找到\t",app,"的路径为：",path)
        # break

from playsound import playsound

# 语音合成的设置
voiceConfig = {
    # 'spd':5,           # 语速，取值0-9，默认为5中语速
    # 'pit':5,           # 音调，取值0 - 9，默认为5中语调
    'vol': 5,  # 音量，取值0 - 15，默认为5中音量
    'per': 4,  # 发音人选择, 0为女声，1为男声，3为情感合成 - 度逍遥，4为情感合成 - 度丫丫，默认为普通女
}
content = "haha"
file = Baymax.creatMP3(content,"test.mp3")
playsound(file)

# if __name__=="__main__":
#     for i in range(1000):
#         print('啦'*i)
    # while True:
    #     print("asdddddddddddddddddddddddddddddddddddddddddddddddd")

#终止软件
# print("关闭QQ音乐")
# os.system("taskkill /F /IM QQMusic.exe")
# print("执行成功")
# path = 'E:Google\\Chrome\\Application\\chrome.exe'
# url = 'http://www.baidu.com/s?wd=美女图片'
# if os.path.isfile(path):
#     webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(path))
#     webbrowser.get('chrome').open_new_tab(url)
# else:
#     webbrowser.open_new_tab(url

# import logging
# import speech-recognition as sr
import speech_recognition as sr
from Niubility import shiyin
from Niubility import luyin
# if __name__ == "__main__":
#     # logging.basicConfig(level=logging.INFO)
#
#     wav_num = 0
#     while True:
#         r = sr.Recognizer()
#         #启用麦克风
#         mic = sr.Microphone()
#         # logging.info('录音中...')
#         print("录音中......")
#         with mic as source:
#             #降噪
#             r.adjust_for_ambient_noise(source)
#             audio = r.listen(source)
#         with open("temp.wav", "wb") as f:
#             #将麦克风录到的声音保存为wav文件
#             f.write(audio.get_wav_data(convert_rate=16000))
#             f.close()
#         # logging.info('录音结束，识别中...')
#         print("录音结束.....")
#         playsound('temp.wav')
#         content = shiyin.shiyin()
#         print("语音内容=",content)

# luyin.luyin()
# content = shiyin.shiyin()
# print(content)