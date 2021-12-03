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
import smtplib
import time
from email.mime.text import MIMEText

from workPlus.MyException import MyException


# ----------------------------------------关于构建上下班时间的操作------------------------------------------------------
# ------------------------------------关于时间的操作-------------------------------------------
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
连接手机
"""
def connectPhone():
    SystemType = "android"
    IP = "127.0.0.1"
    Port = "62001"
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
    device = connectPhone()
    if myTouch("images/workLogo.jpg","点击进入WorkPlus"):
        print("打开workPlus")
        sleep(5)

        if myTouch("images/yingyong.jpg","点击进入应用"):
            print("点击进入应用")
            sleep(3)

            if myTouch("images/kaoqin.jpg","点击进入移动考勤"):
                print("点击进入移动考勤")
                sleep(5)



"""
上班打卡
"""
def goToClockOn():
    print("上班打卡")
    try:
        goAttendancePage()
        reLocation = exists(Template("images/reLocation.png"))
        i = 10
        while reLocation and i > 0:
            myTouch("images/reLocation_touch.png", "点击重新定位")
            sleep(2)
            i=i-1
            reLocation = exists(Template("images/reLocation.png"))
        myTouch("images/goOffClockOn.png", "点击上班打卡")
        # print("点击上班打卡")
        sleep(2)
        goToClockOn_success = exists(Template("images/goToClockOn_success.png"))
        if goToClockOn_success:
            sendEmail(getLocalTime() + "\t上班打卡成功")
        else:
            sendEmail(getLocalTime() + "\t上班打卡失败")
    except (MyException, Exception) as e:
        print("------------------------------------------------------------------------------")
        print("Err==", e)
        sendEmail('上班打卡Err', e)



"""
下班打卡
"""
def goOffClockOn():
    print("下班打卡")
    try:
        goAttendancePage()
        reLocation = exists(Template("images/reLocation.png"))
        i = 10;
        while reLocation and i > 0:
            myTouch("images/reLocation_touch.png","点击重新定位")
            sleep(2)
            i=i-1
            reLocation = exists(Template("images/reLocation.png"))
        # myTouch("images/goOffClockOn.png","点击下班打卡")
        print("点击下班打卡")
        # goOffClockOn_success = exists(Template("images/"))
        # if goOffClockOn_success:
        sendEmail(getLocalTime() + "\t下班打卡成功")
        # else:
        #     sendEmail(getLocalTime() + "\t下班打卡失败")
    except (MyException, Exception) as e:
        print("------------------------------------------------------------------------------")
        print("Err==", e)
        sendEmail('下班打卡Err', e)

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


"""
获取本地格式化时间
"""
def getLocalTime():
    localTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return localTime

"""
    发送邮件到指定邮箱

    @param subject：邮件名
    @param msg：邮件内容
    @param receivers：收件人邮箱列表
"""


def sendEmail(subject, msg, receivers=['end_byfan@163.com']):
    mail_host = 'smtp.163.com'  # 服务器地址
    mail_user = 'f18739427290@163.com'  # 发送者邮箱用户名
    mail_pwd = 'NDPOIQABMUJMJLND'  # 发送者邮箱的SMTP授权码

    sender = 'f18739427290@163.com'  # 发送者邮箱
    receivers = ['end_byfan@163.com']           # 接收者邮箱列表

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式(也有html)，第三个 utf-8 设置编码
    message = MIMEText(msg, 'plain', 'utf-8')

    message['Subject'] = subject  # 设置邮件标题
    message['From'] = sender  # 设置发送人
    message['To'] = receivers       # 设置接收者

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 连接到服务器  ，25为163邮箱的SMTP端口
        smtpObj.login(mail_user, mail_pwd)  # 登录到服务器

        # 批量发送邮件
        for receiver in receivers:
            message['To'] = receiver  # 设置接收者
            smtpObj.sendmail(sender, receiver, message.as_string())

        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("邮件发送失败")
        print("error", e)


if __name__ == "__main__":
    print("Hello Word!")

    # init_device()
    # device_1 = connect_device('android:///127.0.0.1:62001?cap_method=javacap&touch_method=adb')
    # touch(Template('workLogo.jpg'))
    # touch(Template('gaode.jpg'))
    # sleep(1)
    # # touch(Template('kaoqin.jpg'))
    # touch(Template('yingYong.jpg'))
    # home()

    device = connectPhone()
    myTouch("images/workLogo.jpg","点击进入workPlus")
    home()

    print(creatGoToWorkTime())

    # # 开启定时任务
    # scheduler = BlockingScheduler()
    # # 定时上班打卡
    # scheduler.add_job(goToWork(), 'cron', hour=9, minute=40)
    # # 定时下班打卡
    # scheduler.add_job(goOffWork(),'cron', hour=18,minute=15)
    # scheduler.start()



