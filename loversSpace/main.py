# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  main.py    
@Desc   :  
@Author :  ByFan
@Time   :  2021/8/29 16:39 
'''

from airtest.core.api import *

SystemType = "android"
IP = "127.0.0.1"
Port = "62001"


if __name__ == "__main__":
    print("Hello Word!")

    device = connect_device(SystemType + ":///" + IP + ":" + Port + "?cap_method=javacap&touch_method=adb")
    print("返回Home页")
    home()
    loversSpace = exists(Template("images/loversSpace_logo.jpg"))
    if loversSpace:
        print("打开情侣空间")
        touch(loversSpace)
        sleep(10)
        # skip = exists(Template("images/skip.jpg"))
        # if skip:
        #     touch(skip)
        try:
            cancel_1 = exists(Template("images/cancel.jpg"))
        except Exception as e:
            print("aaaaaaaaaa=",e)
        if cancel_1:
            print("点击×")
            touch(cancel_1)
            sleep(1)
        try:
            missYou = exists(Template("images/missYou.jpg"))
            if missYou:
                print("点击每天想你")
                touch(missYou)
                sleep(2)
        except Exception as e:
            print("bbbbbbbb=",e)
        print("点击我们的小世界")
        try:
            world = exists(Template("images/world.jpg"))
            print("world====",world)
            touch(Template("images/world.jpg"))
        except Exception as e:
            print("cccccc=",e)



    # touch(Template("images/tree.jpg"))
    # touch(Template("images/waterDrop.jpg"))
    #
    # touch(Template("images/sun.jpg"))
    #
    # touch(Template("images/redHeart.jpg"))