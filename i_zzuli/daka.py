# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  daka.py    
@Time   :  2021/1/21 13:05 
@Author :  ByFan
'''
from time import sleep
from os import path,system

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
    初次使用进行信息的输入
'''
def firstUse():
    print("第一次使用请输入相关信息:")
    browser = int(input("选择使用的浏览器(电脑已装):\n1.谷歌浏览器\t2.火狐浏览器\t3(默认).Microsoft Edge\n"))
    if browser in [1,2,3]:
        info['browser'] = browser
    username = input("请输入登录用户名：")
    info['username'] = username
    password = input("请输入登录密码：")
    info['password'] = password

    tel = input("请输入联系电话：")
    info['tel'] = tel
    homeTel = input("请输入家庭联系电话：")
    info['homeTel'] = homeTel
    space = input("请输入目前位置和居住地点：")
    info['space'] = space

    # print(info)

    print("信息输入完成。")
    print("其他无特殊情况全部按正常情况进行打卡！")

'''
    加载配置文件
'''
def loadInfo():
    global info
    # 如果没有配置文件则代表第一次使用，那么就创建配置文件，并且输入相关信息
    if not path.isfile(r"i_zzuli.info"):
        firstUse()
        fd = open("i_zzuli.info", mode="w+", encoding="utf-8")
        fd.write(str(info))  # 将字典格式的转换成字符串进行写入
        fd.close()
    # 如有配置文件存在则代表不是第一次使用，那么直接读取配置文件的相关信息
    else:
        fd = open("i_zzuli.info", mode="r+", encoding="utf-8")
        info = eval(fd.read())  # 将读出的字符串转换成字典格式
        fd.close()
        # print("信息加载完毕！")


'''
    根据配置选择浏览器
'''
def chooseWeb(browser=3):

    # 选择浏览器进行启动
    if browser == 3:
        edge_driver = r'./msedgedriver.exe'
        driver = webdriver.Edge(executable_path=edge_driver)
    elif browser == 1:
        # 配置浏览器驱动
        chrome_driver = r'./chromedriver.exe'
        # 打开浏览器
        driver = webdriver.Chrome(executable_path=chrome_driver)
    elif browser == 2:
        firefox_driver = r'./geckodriver.exe'
        driver = webdriver.Firefox(executable_path=firefox_driver)
    return driver

'''
    在浏览器中控制文本框的输入
'''
def ctrlinput(xPathObject,key):
    xPathObject.click()
    xPathObject.clear()
    xPathObject.send_keys(key)


'''
    进行登录系统
'''
def login(username,password):
    # 输入用户名
    username_Input = driver.find_element_by_id('username')
    ctrlinput(username_Input,username)

    # 输入密码
    password_Input = driver.find_element_by_id('password')
    password_Input.send_keys(password)

    driver.execute_script('window.scrollTo(2300,0);')
    sleep(1)
    # 登录
    denglu = driver.find_element_by_xpath('//input[@class=\'qy-log-btn is-on\']')
    # denglu.send_keys(Keys.SPACE)
    # driver.execute_script("$(arguments[0]).click()",denglu)
    denglu.click()

'''
    输入相关信息自动打卡
'''
def daka():
    # 点击打卡
    driver.find_element_by_xpath('//a').click()
    sleep(1)

    # 输入电话
    tel_Input = driver.find_element_by_xpath('//div[10]//input')
    ctrlinput(tel_Input,info['tel'])
    sleep(1)
    # 输入家长电话
    homeTel_Input = driver.find_element_by_xpath('//div[11]//input')
    ctrlinput(homeTel_Input,info['homeTel'])
    sleep(1)
    # 获取位置
    space = driver.find_element_by_xpath('//div[1]/div/div[@class=\'van-cell van-cell--clickable van-field van-field--min-height\']//textarea').click()
    sleep(1)
    # 确认位置
    space_Ok = driver.find_element_by_xpath('//div[2]/div/div/div[2]//i').click()
    sleep(1)
    # 有无症状
    zhengzhuang_No = driver.find_element_by_xpath('//div[1]/div[@class=\'van-checkbox__icon van-checkbox__icon--round\']/i').click()
    sleep(1)
    # 同住人员状况
    tongzhu_No = driver.find_element_by_xpath('//div[10]//div[1]/div/i').click()
    sleep(1)
    # 是否确诊过
    queren_No = driver.find_element_by_xpath('//div[18]//div[1]/div/i').click()
    sleep(1)
    # 其他说明
    other = driver.find_element_by_xpath('//div[23]//textarea')
    ctrlinput(other,'无')
    sleep(1)

    # 提交信息
    tijiao = driver.find_element_by_xpath('//button').click()
    sleep(1)

    # 确认信息
    driver.find_element_by_xpath('//button[@class=\'van-button van-button--default van-button--large van-dialog__confirm van-hairline--left\']').click()


if __name__ == '__main__':
    # 相关信息
    info = {'browser': 3}

    # 驱动文件名称
    webDrivers = ['chromedriver.exe','geckodriver.exe','msedgedriver.exe']
    try:
        # 加载配置文件
        loadInfo()
        # print(info)

        # 选择浏览器打开
        driver = chooseWeb(info['browser'])
        # 最小化窗口
        # driver.minimize_window()
        driver.maximize_window()
        # 访问地址
        driver.get("https://msg.zzuli.edu.cn/xsc/view")

        sleep(1)
        login(info['username'],info['password'])

        sleep(1)
        daka()

        sleep(3)
        driver.close()
        system("taskkill /F /IM " + webDrivers[info['browser']-1])
    except Exception as ex:
        print(ex)
        driver.close()
        print("意外退出！！！\n")
        print("请重新打卡！!")






