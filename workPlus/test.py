# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  test.py    
@Desc   :  
@Author :  ByFan
@Time   :  2021/8/27 15:50 
'''
import datetime
import random
import time

import pmod as pmod
from airtest.core.api import *

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
    return seconds2time(rt)

"""
生成一个上班的随机时间
"""
def creatGoToWorkTime():
    st = "08:50:00"
    et = "09:10:00"
    return randomTime(st,et)

"""
生成一个下班的随机时间
"""
def creatGoOffWorkTime():
    st = "18:20:00"
    et = "18:40:00"
    return randomTime(st,et)



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
    device_1 = connect_device('android:///127.0.0.1:62001?cap_method=javacap&touch_method=adb')
    # touch(Template('workLogo.jpg'))
    touch(Template('gaode.jpg'))
    sleep(1)
    # # touch(Template('weizhi.jpg'))
    # touch(Template('yingyong.jpg'))
    # home()

