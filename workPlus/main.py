# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  main.py
@Desc   :  
@Author :  ByFan
@Time   :  2021/8/27 15:50 
'''
import random

from airtest.core.api import *
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

# ----------------------------------------关于构建上下班时间的操作------------------------------------------------------
from workPlus.MyException import MyException

"""
返回的是a//b（除法取整）以及a对b的余数
"""
def pmod(a,b):
    n = a // b      # 除法取整
    m = a % b
    return n,m

""""
把字符串时间转换成秒
"""
def time2seconds(t):
    h,m,s = t.strip().split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)

"""
把秒转换成字符串时间
"""
def seconds2time(sec):
    m,s = pmod(sec,60)
    h,m = pmod(m,60)
    return "%02d:%02d:%02d" % (h,m,s)

"""
根据两个时间点随机生成一个之间的时间
"""
def randomTime(st,et):
    sts = time2seconds(st)
    ets = time2seconds(et)
    rt = random.sample(range(sts,ets),1)
    return seconds2time(rt[0])

"""
生成一个上班的随机时间
"""
def creatGoToWorkTime():
    st = "08:45:00"
    et = "09:10:00"
    date = time.strftime("%Y-%m-%d ", time.localtime())
    dateTime = date + randomTime(st, et)
    return dateTime

"""
生成一个下班的随机时间
"""
def creatGoOffWorkTime():
    st = "18:20:00"
    et = "19:30:00"
    date = time.strftime("%Y-%m-%d ",time.localtime())
    dateTime = date+randomTime(st,et)
    return dateTime

# ------------------------------------关于打卡的操作-------------------------------------------

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
        sleep(1)
        return True
    except Exception:
        print(msg + '失败')
        raise MyException(msg + '失败')
        return False

"""
进入到打卡页面
"""
def goAttendancePage():
    print("")


"""
上班打卡
"""
def goToClockOn():
    print("上班打卡")



"""
下班打卡
"""
def goOffClockOn():
    print("下班打卡")

# ------------------------------关于上下班定时的操作-----------------------------------------

"""
上班
"""
def goToWork():
    print("上班")
    # 创建打卡时间
    dateTime = creatGoToWorkTime()
    # 定时打卡
    sched = BackgroundScheduler()
    sched.add_job(goToClockOn,'date',run_date=dateTime)

"""
下班
"""
def goOffWork():
    print("下班")
    # 创建打卡时间
    dateTime = creatGoOffWorkTime()
    # 定时打卡
    sched = BackgroundScheduler()
    sched.add_job(goOffClockOn, 'date', run_date=dateTime)




if __name__ == "__main__":
    print("Hello Word!")
    # lt = time.localtime()
    # ltstr = time.strftime("%H:%M:%S",lt)
    # print(ltstr)
    # st = "17:46:00"
    # while(ltstr != st):
    #     ltstr = time.strftime("%H:%M:%S",time.localtime())
    # print(ltstr)

    # init_device()
    # device_1 = connect_device('android:///127.0.0.1:62001?cap_method=javacap&touch_method=adb')
    # touch(Template('workLogo.jpg'))
    # touch(Template('gaode.jpg'))
    # sleep(1)
    # # touch(Template('weizhi.jpg'))
    # touch(Template('yingYong.jpg'))
    # home()
    # print(3//2)
    # print(seconds2time(3700))

    print(creatGoToWorkTime())

    # # 开启定时任务
    # scheduler = BlockingScheduler()
    # # 定时上班打卡
    # scheduler.add_job(goToWork(), 'cron', hour=9, minute=40)
    # # 定时下班打卡
    # scheduler.add_job(goOffWork(),'cron', hour=18,minute=15)
    # scheduler.start()



