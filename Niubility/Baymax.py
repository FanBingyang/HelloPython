import requests
import json
from aip.speech import AipSpeech
from playsound import playsound
import os
import webbrowser
import threading
import time

from Niubility import luyin
from Niubility import shiyin

"""
功能：对话机器人，根据用户提问返回相应的对话
传参：data：用户对话的内容
返回：机器人会话内容
"""
def robot(data):
    # 图灵机器人用户信息
    TULING_APIKEY = '586947b0e57d4322912768e3b7662881'
    # TULING_APIKEY = '4cb32264c45e43968026624fc078f1a2'
    TULING_USERID = '544086'
    urls = 'http://openapi.tuling123.com/openapi/api/v2'


    # 请求信息格式1
    data_dict = {
        "reqType":0,
        "perception":{
            "inputText":{
                "text":data
            },
        },
        "userInfo":{
            "apiKey":TULING_APIKEY,
            "userId":TULING_USERID
        }
    }

    # 请求信息格式2
    # jsjs = {
    #     "key": '586947b0e57d4322912768e3b7662881',
    #     "info": "鱼香肉丝怎么做"
    # }
    # result = requests.post("http://www.tuling123.com/openapi/api", json=jsjs)

    # 发送post请求
    try:
        result = requests.post(urls,json=data_dict)
    except:
        result = "哎呀，网络好像出了点问题"
        return result
    # 获取请求返回信息
    content = (result.content).decode('utf-8')
    # 将返回信息转成json格式
    content = json.loads(content)
    # print('content=',content)
    # 从数据中找到需要的文本信息
    # 搜素图片时该匹配语法不正确，待修复
    try:
        result = content['results'][0]['values']['text']
    except:
        result = "你说的什么？我没有听清。"
        return result
    return result

"""要合成语音的文字内容
功能：语音合成，返回合成的文件路径
传参：data：
返回：合成音频的文件名
"""
def creatMP3(data,fileName = "source/temp.mp3"):
    # 百度语音用户信息
    APP_ID = '18177332'
    API_KEY = 'NLCIQxoW6uAjPI61I4z0XOho'
    SECRET_KEY = 'q4XYOgBDP3fMljuOD7Rl1ij1WN2Lq6Ig'

    # 设置保存音频文件名
    # fileName = f"error_{voiceConfig['per']}.mp3"

    # 创建客户端
    clint = AipSpeech(APP_ID,API_KEY,SECRET_KEY)


    # 进行语音合成
    try:
        result = clint.synthesis(data,'zh',1,voiceConfig)
    except:
        fileName = f"{SOURCE_PATH}error_{voiceConfig['per']}.mp3"
        return fileName

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result,dict):
        with open(fileName,'wb') as f:
            f.write(result)
            f.close()
    # else:
    #     fileName = f"error_{voiceConfig['per']}.mp3"
    return fileName

    # dict
    # // 成功返回二进制文件流
    # // 失败返回
    # {
    #     "err_no":500,
    #     "err_msg":"notsupport.",
    #     "sn":"abcdefgh",
    #     "idx":1
    # }

"""
功能：进行音频播放，并删除播放的音频文件
传参：fileName：播放音频的路径
返回：无
"""
def soundMP3(fileName):
    playsound(fileName)
    # os.remove(fileName)

"""
功能：查找指定软件的执行文件的路径
传参：path：扫描的路径
      appName：查找的软件名称
返回：软件的绝对路径
"""
def findPath(path,appName):
    # 遍历返回的是一个三元组(root,dirs,files)
    # root 所指的是当前正在遍历的这个文件夹的本身的地址
    # dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
    # files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
    for root, dirs, files in os.walk(path):
        if appName in dirs or appName in files:
            # root = str(root)
            return os.path.join(root, appName)
    else:
        return False

"""
功能：查找软件路径的线程执行程序
传参：app：要查找路径的软件执行名称
返回：无
"""
def run(volList,appNameLIst):
    # print("开始\t",app,"\t的查找。。。")


    # 挨个盘符进行遍历寻找软件的路径
    for app in appNameLIst:
        for vol in volList:
            # time.sleep(1)
            path = findPath(vol,app)
            if path:
                # 找到路径之后，保存到软件路径字典中
                APP_PATH_LIST[app] = path
                # print("run_____APP_PATH_LIST==",APP_PATH_LIST)
                # print("找到\t",app,"的路径为：",path)

"""
功能：判断线程的执行程序，判断其他子线程是否执行完毕，并对软件路径文本进行操作。
传参：threads：其他子线程的列表
返回：无
"""
def run2(threads):
    # print("判断线程开启")
    for t in threads:
        t.join()
    # print("子线程全部结束")
    file = open(appPathList_File,'w')
    file.write(json.dumps(APP_PATH_LIST))
    file.close()
    print("大白：扫描完成")


def run3():
    playsound(f"{SOURCE_PATH}sleep_{voiceConfig['per']}.mp3")
    print("大白：休眠中...")
    keywords = ['你好大白','大白你好','大白菜吗']
    while True:
        # print("休眠中....")
        luyin.luyin()
        # print(threading.current_thread().getName(),"========",threading.current_thread().is_alive())
        try:
            # 对音频文件进行识别
            result = shiyin.shiyin()
            result = json.loads(result)
            # 获取用户指令
            result = result['result'][0]
            # print("result==",result)
        except:
            # 如果获取出问题则默认用户没有发出指令
            # print(threading.current_thread().getName(), "运行结束")
            continue
        if result in keywords:
            if result == '大白菜吗':
                result = '大白在吗'
            print("你：",result)
            flieName = creatMP3('主人你好啊，请问您有什么吩咐？')
            print("大白：主人你好啊，请问您有什么吩咐？")
            playsound(flieName)
            break
    Main()


def Main():
    # 主体运行
    while True:
        # data = input("你：")
        # print("开始录音")
        # 进行录音，采取用户指令
        luyin.luyin()
        # print("录音完成，开始识别")
        try:
            # 对音频文件进行识别
            result = shiyin.shiyin()
            result = json.loads(result)
            # print("识别完成")
            # 获取用户指令
            result = result['result'][0]
        except:
            # 如果获取出问题则默认用户没有发出指令
            try:
                threading.Thread(target=run3(), args=()).start()
            except:
                return
            break
        print("你：",result)

        # “退出”指令，关闭当前程序
        if "退出" in result:
            print("大白：好的，期待下次为您服务，拜拜啦！")
            playsound(f"{SOURCE_PATH}bye_{voiceConfig['per']}.mp3")
            break

        # “打开”指令，可以打开电脑上的指定软件
        if "打开" in result:
            # 执行打开软件，并返回打开的状态
            content = runAPP(result)
            # 语音播报
            Say(content)
            continue

        # “关闭”指令，可以关闭电脑上的指定软件
        if "关闭" in result:
            # 执行关闭软件，并返回操作的状态
            content = exitAPP(result)
            # 语音播报
            Say(content)
            continue

        # “搜索”指令，打开浏览器进行关键字搜索
        if "搜索" in result:
            # 执行搜索，并返回操作状态
            content = search(result)
            # 语音播报
            Say(content)
            continue

        # 调用机器人接口，获得对话内容
        try:
            content = robot(result)
            if content == "请求次数超限制":
                content = robot(result)
        except:
            print("大白：哎呀，网络好像出了点问题")
            playsound(f"{SOURCE_PATH}error_{voiceConfig['per']}.mp3")
            continue
        # 语音播报
        Say(content)

"""
功能：打开指定电脑上的软件
传参：appName：要打开的软件名称
返回：执行状态
"""
def runAPP(appName):

    flag = "打开成功！"

    star = int(appName.find("打开"))
    # 获取要打开的软件名称
    appName = appName[star + 2:]

    if appName == "浏览器":
        try:
            webbrowser.open("http://www.baidu.com")
        except:
            flag = "抱歉，打开失败了呢！"
            return flag
        return flag

    # 判断是否支持该软件的打开
    if appName in APP_NAME_LIST.keys():
        app = APP_NAME_LIST[appName]
        # 获取要打开的软件路径
        appPath = APP_PATH_LIST[app]
        # 判断本机是否有该软件的路径
        if appPath == '':
            flag = "抱歉，没有找到相关软件！"
        else:
            # 打开软件
            try:
                os.startfile(appPath)
            except:
                flag = "抱歉，打开失败了呢！"
                return flag
    else:
        flag = "抱歉，我还不支持打开这个软件，我会慢慢升级的！"

    return flag

"""
功能：关闭指定软件
传参：appName：要关闭的软件名称
返回：执行状态
"""
def exitAPP(appName):
    flag = "关闭成功！"

    star = int(appName.find("关闭"))
    # 获取要打开的软件名称
    appName = appName[star + 2:]

    if appName == "浏览器":
        try:
            os.system("taskkill /F /IM MicrosoftEdge.exe")
        except:
            flag = "抱歉，关闭失败了呢！"
            return flag
        return flag

    # 判断是否支持该软件的关闭
    if appName in APP_NAME_LIST.keys():
        app = APP_NAME_LIST[appName]
        try:
            os.system("taskkill /F /IM " + app)
        except:
            flag = "抱歉，关闭失败了呢！"
            return flag
    else:
        flag = "抱歉，我还不支持操作这个软件，我会慢慢升级的！"

    return flag

"""
功能：根据用户的搜索指令，打开浏览器进行百度搜索
传参：content：用户的搜索指令
返回：执行状态
"""
def search(content):
    flag = "已经为您找到搜索结果，请查看！"

    # 获取要搜索的内容
    star = int(content.find("搜索"))
    content = content[star + 2:]
    # 拼接百度搜索的url
    url = 'http://www.baidu.com/s?wd=' + content
    # 获取谷歌浏览器的执行路径
    chromePath = APP_PATH_LIST['chrome.exe']
    # 判断获取到的执行路径是否存在
    if os.path.isfile(chromePath):
        # 注册谷歌浏览器
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
        try:
            # 打开浏览器执行搜索
            webbrowser.get('chrome').open_new_tab(url)
        except:
            # 如果打开失败就用默认浏览器打开
            try:
                webbrowser.open_new_tab(url)
            except:
                # 默认浏览器打开失败，返回无法打开。
                flag = "浏览器打开失败，无法进行搜索！"
                return flag
    else:
        # 如果执行浏览器不存在，那么就用默认浏览器进行搜索
        try:
            webbrowser.open_new_tab(url)
        except:
            # 默认浏览器打开失败，返回无法打开。
            flag = "浏览器打开失败，无法进行搜索！"
            return flag

    return flag


"""
功能：接收大白响应的内容，进行播放，同时打印到控制台
传参：content：大白响应的内容
返回：无
"""
def Say(content):
    # 进行语音合成
    filmName = creatMP3(content)
    # 输出结果
    print("大白：",content)
    # 播放语音
    playsound(filmName)
    # playsound在执行完播放之后不会自动关闭或释放打开的文件，
    # 需要找到该模块位置，在模块中相应位置添加winCommand('close', alias)，这样在调用后就会自动关闭文件，防止在此操作该文件而报错
    # if block:
    #     sleep(float(durationInMS) / 1000.0)
    #     # 播放后，关闭该文件
    #     winCommand('close', alias)

"""
功能：如果appPathList_File.txt文件不存在，则创建文件；如果该文件存在，从中读取软件路径
传参：无
返回：无
"""
def readPathList(APP_PATH_LIST):
    # 判断是否存在当前文件
    if not os.path.isfile(appPathList_File):
        # print("没有找到txt文件")
        # 没有找到文件，创建新文件
        file = open(appPathList_File, 'w', encoding='utf-8')
        file.close()
    else:
        # print("找到了txt文件")
        # 找到文件，读取文件内容
        file2 = open(appPathList_File, 'r')
        js = file2.read()
        # print('file2.read()=====',js)
        # 判断文件内容是否为空，不为空则进行赋值
        if js != '':
            APP_PATH_LIST = json.loads(js)
            # print('appPath_List======',APP_PATH_LIST)
        file2.close()
    return APP_PATH_LIST

"""
功能：开启所有子线程，包括扫描获取软件路径的线程，和判断扫描线程结束的线程
传参：无
返回：无me
"""
def starThread():
    # 扫描线程的线程池
    threads = []
    # 创建扫描线程，开始扫描获取软件路径
    # try:
    #     for app in APP_PATH_LIST:
    #         t = threading.Thread(target=run, args=(app,))
    #         t.start()
    #         threads.append(t)
    # except:
    #     print(app, "的查找线程创建失败")
    # 盘符列表
    volList = []
    # 遍历字母A到Z，忽略光驱的盘符，找到用户当前正在使用的盘符
    for i in range(65, 91):
        vol = chr(i) + ':'
        if os.path.isdir(vol):
            volList.append(vol)
    try:
        t = threading.Thread(target=run,args=(volList,APP_PATH_LIST.keys(),))
        t.start()
        threads.append(t)
    except:
        t = threading.Thread(target=run, args=(APP_PATH_LIST,))
        t.start()
        threads.append(t)

    # 创建判断线程，用于判断其他子线程是否执行完毕
    try:
        threading.Thread(target=run2, args=(threads,)).start()
    except:
        # print("判断线程运行情况的线程出现问题")
        threading.Thread(target=run2, args=(threads,)).start()


"""
大白运行的主函数
"""
if __name__=="__main__":

    SOURCE_PATH = "source/"

    # 语音合成的设置
    voiceConfig = {
        # 'spd':5,           # 语速，取值0-9，默认为5中语速
        # 'pit':5,           # 音调，取值0 - 9，默认为5中语调
        'vol': 5,  # 音量，取值0 - 15，默认为5中音量
        'per': 0,  # 发音人选择, 0为女声，1为男声，3为情感合成 - 度逍遥，4为情感合成 - 度丫丫，默认为普通女
    }


    # 支持打开/关闭的软件
    APP_NAME_LIST = {'QQ': 'QQ.exe', 'tim': 'TIM.exe', '微信': 'WeChat.exe',
                    'QQ音乐': 'QQMusic.exe', '网易音乐': 'cloudmusic.exe',
                    '腾讯视频': 'QQLive.exe', '爱奇艺': 'QyClient.exe',
                    '谷歌浏览器': 'chrome.exe', '火狐浏览器': 'firefox.exe'
                    }
    # 软件路径
    APP_PATH_LIST = {'QQ.exe': '', 'TIM.exe': '', 'WeChat.exe': '',
                    'QQMusic.exe': '', 'cloudmusic.exe': '',
                    'QQLive.exe': '', 'QyClient.exe': '',
                    'chrome.exe': '', 'firefox.exe': ''
                    }
    # 保存软件路径的文本文件
    appPathList_File = f'{SOURCE_PATH}appPath_List.txt'

    # 从文件中读取软件路径
    APP_PATH_LIST = readPathList(APP_PATH_LIST)
    # print(APP_PATH_LIST)
    # 开启扫描线程和扫描线程的判断线程
    starThread()

    # 欢迎语
    print("大白：亲爱的主人您好啊，我是大白，有什么可以帮助您的嘛？")
    playsound(f"{SOURCE_PATH}welcome_{voiceConfig['per']}.mp3")

    # 主体运行
    Main()






