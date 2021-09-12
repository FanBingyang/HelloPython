# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  dingshi.py    
@Time   :  2021/2/13 18:10 
@Author :  ByFan
'''
import time,os,sched
schedule = sched.scheduler(time.time,time.sleep)
#定时执行任务命令

# def perform_command(cmd,inc):
#     os.system(cmd)
#     print('task')
# def timming_exe(cmd,inc=60):
#     schedule.enter(inc,0,perform_command,(cmd,inc))
#     schedule.run()
# print('show time after 2 seconds:')
# timming_exe('echo %time%',2)

# def perform_command(cmd,inc):
#   #在inc秒后再次运行自己，即周期运行
#   schedule.enter(inc, 0, perform_command, (cmd, inc))
#   os.system(cmd)
# def timming_exe(cmd,inc=60):
#   schedule.enter(inc,0,perform_command,(cmd,inc))
#   schedule.run()#持续运行，直到计划时间队列变成空为止
# print('show time after 2 seconds:')
# timming_exe('echo %time%',2)

import time,os
def re_exe(cmd,inc = 60):
  while True:
    os.system(cmd)
    time.sleep(inc)
re_exe("echo %time%",5)