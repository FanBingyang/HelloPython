# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  main.py    
@Time   :  2021/9/23 14:31 
@Author :  ByFan
'''
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import zmail

"""
测试发送带图片的邮件，返回包装好的message
"""
def addImage(sender,receivers):
    msg = '这是一个测试图片的邮件<br>' \
          '<p><img src="cid:image"></p><br>'
    message = MIMEMultipart('related')
    message['Subject'] = '测试图片邮件'
    message['From'] = sender
    message['To'] = receivers[0]
    msgAlternative = MIMEMultipart('alternative')
    message.attach(msgAlternative)
    msgAlternative.attach(MIMEText(msg, 'html', 'utf-8'))
    fp = open('16.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<image>')
    message.attach(msgImage)
    return message

"""
    发送邮件到指定邮箱
    
    @param subject：邮件名
    @param msg：邮件内容
    @param receivers：收件人邮箱列表
"""
def sendEmail(subject,msg,receivers=['end_byfan@163.com']):
    mail_host = 'smtp.163.com'                   # 服务器地址
    mail_user = 'f18739427290@163.com'          # 发送者邮箱用户名
    mail_pwd = 'NDPOIQABMUJMJLND'               # 发送者邮箱的SMTP授权码

    sender = 'f18739427290@163.com'             # 发送者邮箱
    # receivers = ['end_byfan@163.com']           # 接收者邮箱列表

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式(也有html)，第三个 utf-8 设置编码
    message = MIMEText(msg,'plain','utf-8')

    message['Subject'] = subject    # 设置邮件标题
    message['From'] = sender        # 设置发送人
    # message['To'] = receivers       # 设置接收者


    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host,25)       # 连接到服务器  ，25为163邮箱的SMTP端口
        smtpObj.login(mail_user,mail_pwd)   # 登录到服务器

        # 批量发送邮件
        for receiver in receivers:
            message['To'] = receiver  # 设置接收者
            smtpObj.sendmail(sender,receiver,message.as_string())

        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("邮件发送失败")
        print("error",e)

def getEmail():
    mail_user = "end_byfan@163.com"
    mail_pwd = "GUMAGCDWHGEUSBOV"
    mail_server = zmail.server(mail_user,mail_pwd)
    mail = mail_server.get_latest()
    zmail.show(mail)
    print("---------------------------------------------")
    print(mail['Subject'])
    print(mail['From'])
    print(mail['To'])
    print(mail['Date'])
    print(mail['Content_text'])
    print(mail['Content_html'])
    print(mail['Attachments'])

def getLocalTime():
    localTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return localTime

if __name__ == '__main__':
    print("Hello python!")
    # operationEmail()

    # getEmail()

    print(getLocalTime())
