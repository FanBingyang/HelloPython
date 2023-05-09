# coding=utf-8
"""
    @Author：byFan
    @FileName： ikuuu.py
    @Date：2023/5/8
    @Describe: 
"""
import json
import os
import random
import smtplib
import time
from email.mime.text import MIMEText

import requests


class Ikuuu:
    email = None
    passwd = None
    cookie = None
    notifyEmail = None

    def __init__(self, confInfo):
        self.email = confInfo['email']
        self.passwd = confInfo['passwd']
        self.cookie = confInfo['cookie']
        self.notifyEmail = confInfo['notify-email']

    def run(self):
        """
        主体运行方法
        @return:
        """
        self.isCookie()
        self.clockIn()

    def isCookie(self):
        """
        校验配置文件中的是否有可用的cookie，如果没有的话就通过登录再获取一个可用的cookie
        @return:
        """
        if self.cookie is None or self.cookie == '':
            self.signIn()
        else:
            timestamp = int(time.time())
            cookieDict = dict(item.split("=") for item in self.cookie.split(";"))
            expire_in_ = cookieDict['expire_in']
            if expire_in_ is None or int(expire_in_) <= timestamp:
                self.signIn()

    def signIn(self):
        """
        进行登录，并且保存cookie信息到配置文件
        @return:
        """
        print("signIn")
        url = "https://ikuuu.eu/auth/login"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Content-Type': 'application/json'
        }
        body = json.dumps(self.__dict__)
        response = requests.post(url, headers=headers, data=body)
        if response.status_code == 200:
            contentDict = json.loads(response.content.decode())
            print("contentDict = ", contentDict)
            if contentDict['ret'] == 1:
                cookies_dict = response.cookies.get_dict()
                cookieStr = ";".join([f'{k}={v}' for k, v in cookies_dict.items() if k != 'ip'])
                self.cookie = cookieStr
                with open(CONF_PATH, "w") as f:
                    json.dump(self.__dict__, f)
            else:
                raise XException(FAIL_CONTENT % (self.email, "登录失败", contentDict['msg']), self.notifyEmail)
        else:
            raise XException(FAIL_CONTENT % (self.email, "登录失败", response.content.decode()), self.notifyEmail)

    def clockIn(self):
        """
        进行ikuuu签到，然后将结果发送至邮箱
        @return:
        """
        url = "https://ikuuu.eu/user/checkin"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Content-Type': 'application/json',
            'Cookie': self.cookie
        }
        response = requests.post(url, headers=headers)
        contentDict = json.loads(response.content.decode())
        if response.status_code == 200:
            msg = contentDict['msg']
            if contentDict['ret'] == 1:
                sendEmail(SUCCESS_CONTENT % (self.email, msg), self.notifyEmail)
            else:
                sendEmail(FAIL_CONTENT % (self.email, "签到请求失败", msg), self.notifyEmail)
        else:
            sendEmail(FAIL_CONTENT % (self.email, "签到请求失败", str(response.content.decode())), self.notifyEmail)


class XException(Exception):
    """
    自定义异常类
    """

    def __init__(self, err='XExceptionErr', notifyEmail=''):
        self.err = err
        self.notifyEmail = notifyEmail
        Exception.__init__(self, err)

    def __str__(self):
        print("XException: ", self.err)
        sendEmail(self.err, self.notifyEmail)


def readFile(filePath):
    """
    读取配置文件, 返回文件内容
    @param self:
    @return:
    """
    if os.path.exists(filePath):
        with open(filePath, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
            return data
    else:
        raise XException(FAIL_CONTENT % ("Admin", "读入配置文件失败", "配置文件不存在"))


def sendEmail(msg, receiver, subject="ikuuu签到通知"):
    """
    发送邮件
    @param receiver: 接收者邮箱
    @param subject: 主题
    @param msg: 内容
    @return:
    """

    adminEmail = "notify_v@163.com"
    # 接收者邮箱列表
    receivers = []
    if receiver is not None:
        receivers.append(receiver)
    else:
        receivers.append(adminEmail)
    if adminEmail not in receivers:
        receivers.append(adminEmail)

    emailConfPath = "email_conf"
    with open(emailConfPath, "r", encoding="utf-8-sig") as f:
        emailConf = json.load(f)
    mail_host = emailConf['host']
    mail_user = emailConf['user']
    mail_passwd = emailConf['passwd']

    sender = emailConf['sender']  # 发送者邮箱

    msg = msg + ("时间：%s\n" % getLocalTime())
    print(msg)
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式(也有html)，第三个 utf-8 设置编码
    message = MIMEText(msg, 'plain', 'utf-8')

    message['Subject'] = subject  # 设置邮件标题
    message['From'] = sender  # 设置发送人

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 连接到服务器  ，25为163邮箱的SMTP端口
        smtpObj.login(mail_user, mail_passwd)  # 登录到服务器

        # 批量发送邮件
        for receiver in receivers:
            message['To'] = receiver  # 设置接收者
            # smtpObj.sendmail(sender, receiver, message.as_string())

        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("邮件发送失败")
        print("error", e)


def getLocalTime():
    """
    获取当前时间，返回格式化之后的时间
    @return:
    """
    localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return localTime


if __name__ == '__main__':
    FAIL_CONTENT = "用户：%s\n结果：ikuuu签到失败\n详情：%s\n原因：%s\n"
    SUCCESS_CONTENT = "用户：%s\n结果：ikuuu签到成功\n详情：%s\n"
    CONF_PATH = "conf.json"
    confList = readFile(CONF_PATH)
    for conf in confList:
        ikuuu = Ikuuu(conf)
        ikuuu.run()
        randnum = random.randint(1, 5)
        time.sleep(randnum * 60)
