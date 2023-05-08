# coding=utf-8
"""
    @Author：byFan
    @FileName： ikuuu.py
    @Date：2023/5/8
    @Describe: 
"""
import json

import requests


def signIn():
    print("登录")
    url = "https://ikuuu.eu/auth/login"
    email = "byfanx@163.com"
    passwd = "ikuuu170307!"
    data = {}
    data['email'] = email
    data['passwd'] = passwd
    data['code'] = ''

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json'
    }

    session = requests.Session()
    response = session.post(url, headers=headers, data=json.dumps(data))
    print("cookies = ", response.cookies)
    print("status_code = ", response.status_code)
    print("content = ", response.content.decode())
    print("headers = ", response.headers)

    print("type(session) = ", type(session))
    print("session = ", session)
    print("cookies = ", session.cookies)
    print("cookies dict = ", session.cookies.get_dict())


if __name__ == '__main__':
    print("Hello world!")
    signIn()


"""

lang=zh-cn; _ga=GA1.2.1520828038.1678612212; uid=794683; email=byfanx%40163.com; key=a896b3bc3d9eafac27ea94fd067939e8a3b174a91bca6; ip=5f5831ea69fe3e35a8bec93c3824b3da; expire_in=1683772210; _gid=GA1.2.566869352.1683167412; _gat_gtag_UA_158605448_1=1
"""