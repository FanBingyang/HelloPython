# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  test.py    
@Time   :  2021/9/24 16:17 
@Author :  ByFan
'''
from airtest.core.api import *
from airtest.core.android import Android

from workPlus.MyException import MyException

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
            print(msg + '失败')
            return False
    except Exception:
        print(msg + '失败')
        raise MyException(msg + '失败')
        return False

"""
上滑 返回手机主页
"""
def returnHome():
    # 获取手机高度和宽度
    width,height = device.get_current_resolution()
    x1 = width * 0.5
    y1 = height
    y2 = height * 0.5
    swipe([x1,y1],[x1,y2])
    print("上滑 返回手机主页")
    sleep(1)

"""
向左滑
"""
def leftSlide():
    width, height = device.get_current_resolution()
    x1 = width * 0.9
    x2 = width * 0.2
    y1 = height * 0.5
    swipe([x1, y1], [x2, y1])
    print("向左滑动")
    sleep(1)

if __name__ == '__main__':
    print("Hello python!")

    SystemType = "android"
    IP = "192.168.111.185"
    Port = "48887"
    try:
        device = connect_device(SystemType + ":///" + IP + ":" + Port + "?cap_method=javacap&touch_method=adb")

        stop_app("com.foreverht.workplus.v4")

        print("关闭后台workPlus程序")

        home()
        print("返回Home页")

        qqMusic = myTouch("images/qqMusic.jpg","打开QQ音乐")
        if qqMusic:
            puTong = exists(Template("images/puTong.jpg"))
            print("putong==",puTong)

        # 返回手机主页
        returnHome()
        # 左滑 *2
        leftSlide()
        leftSlide()

        workPlus = myTouch("images/workPlus_logo.jpg","打开workPlus")

        if workPlus:
            # yingYong = myTouch("images/yingYong.jpg", "打开应用页面")
            # yingYong2 = myTouch("images/yingYong2.jpg","打开应用页面")
            # kq = exists(Template("images/kaoQin.jpg"))
            # if yingYong or yingYong2 or kq:
            yingyong = touch((742, 2240))
            kaoQin = myTouch("images/kaoQin.jpg", "进入考勤页面")
            if kaoQin:
                print("打卡成功")




    except Exception:
        print("连接手机失败")