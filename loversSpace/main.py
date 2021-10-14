# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  main.py
@Desc   :  
@Author :  ByFan
@Time   :  2021/8/29 16:39 
'''

import time
from airtest.core.api import *
from operationEmail.main import sendEmail
from loversSpace import MyException
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler


SystemType = "android"
IP = "127.0.0.1"
Port = "62001"

"""
连接手机
"""
def connectPhone():
    try:
        device = connect_device(SystemType + ":///" + IP + ":" + Port + "?cap_method=javacap&touch_method=adb")
    except Exception:
        print("连接手机失败")
        raise MyException("连接手机失败")
    return device


"""
自定义点击图标
"""
def myTouch(fileName,msg):
    try:
        element = exists(Template(fileName))
        if element :
            touch(element)
            print("element==",element)
            print(msg)
            sleep(1)
            return True
        else:
            sleep(1)
            print('跳过'+msg)
            return False
    except Exception:
        print(msg + '失败')
        raise MyException(msg + '失败')
        return False


"""
获取本地格式化时间
"""
def getLocalTime():
    localTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return localTime

"""
空间打卡
"""
def zoneClockOn():
    # 连接到手机
    try:
        device = connectPhone()

        stop_app("com.welove520.qqsweet")
        print("关闭后台空间程序")

        home()
        print("返回Home页")
        sleep(1)

        if myTouch("images/loversSpace_logo.jpg","打开情侣空间"):
            sleep(5)

            skipAd = myTouch("images/skip.jpg","点击跳过广告")

            closeGiftBag = myTouch("images/closeGiftBag.jpg","关闭领礼包页")

            closeMiss = myTouch("images/closeMiss.jpg","关闭miss之后的弹窗")

            miss = myTouch("images/missYou.jpg","点击每天想你")

            closeMiss2 = myTouch("images/closeMiss.jpg","关闭miss之后的弹窗")

            word = myTouch("images/world.jpg","进入小世界")
            if word:
                tree = myTouch("images/tree.jpg","进入爱情树")
                if tree:

                    authentication = myTouch("images/authentication.png","暂不实名认证")

                    waterDrop = myTouch("images/waterDrop.jpg","进行浇水")

                    sun = myTouch("images/sun.jpg","进行晒太阳")
                    # sun = touch(589, 407)
                    # print("进行晒太阳")
                    closeRecord = myTouch("images/closeRecord.jpg","关闭浇水记录页面")

                    redHeart = myTouch("images/redHeart.jpg","收集爱心")
                    if redHeart:
                        receive = myTouch("images/receive.jpg","普通领取红心")
            print("空间签到完成！")
            msg = getLocalTime() + '签到成功!'
            # 发送提醒邮件
            sendEmail('空间签到',msg)

            home()
            print("返回Home页")
    except (MyException , Exception) as e:
        print("-------------------------------------------------------------------------------------------------------------")
        print("Err==",e)
        sendEmail('空间签到',e)

if __name__ == "__main__":
    print("Hello Word!")

    # 开启定时任务
    scheduler = BlockingScheduler()
    scheduler.add_job(zoneClockOn(),'cron',hour=9, minute=30)
    scheduler.start()
    # zoneClockOn()
