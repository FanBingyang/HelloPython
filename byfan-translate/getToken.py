# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  getToken.py    
@Desc   :  获取百度api鉴权的token
@Author :  byfan
@Time   :  2022/10/11 16:08 
'''
import json
import os
import time
import requests

def requestToken():
    API_KEY = 'ti1IRb3cqfFZgX921irSCWSe'
    SECRET_KEY = 'WFawYbSg1yyW4ppOIBXaWRTzc5mUXkVf'

    access_token = ''
    expires_in = ''

    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_KEY + '&client_secret=' + SECRET_KEY
    response = requests.get(host)
    if response:
        # print(response.json())
        response_json = response.json()

        access_token = response_json['access_token']
        expires_in = response_json['expires_in']
    return access_token, expires_in

def getToken():
    TOKEN = 'token'
    EFFECTIVE_DURATION = 'effective_duration'
    CREATE_TIME = 'create_time'
    timeStamp = int(time.time())  # 获取当前秒数

    token = ''

    file_name = 'token.json'
    exists = os.path.exists(file_name)
    if exists:
        file_object = open(file_name, 'r+')
        file_dict = json.load(file_object)
        if int(file_dict[CREATE_TIME]) + int(file_dict[EFFECTIVE_DURATION]) > timeStamp:
            token = file_dict[TOKEN]
        else:
            access_token, effective_duration = requestToken()
            file_dict[TOKEN] = access_token
            file_dict[EFFECTIVE_DURATION] = effective_duration
            file_dict[CREATE_TIME] = timeStamp
            token = file_dict[TOKEN]
            # file_object.write(json.dumps(file_dict, indent=4, ensure_ascii=False))   # 与下方等价
            json.dump(file_dict, file_object, indent=4, ensure_ascii=False)
    else:
        file_object = open(file_name, 'w')
        file_dict = {}
        access_token, effective_duration = requestToken()
        file_dict[TOKEN] = access_token
        file_dict[EFFECTIVE_DURATION] = effective_duration
        file_dict[CREATE_TIME] = timeStamp
        token = file_dict[TOKEN]
        # file_object.write(json.dumps(file_dict, indent=4, ensure_ascii=False))   # 与下方等价
        json.dump(file_dict, file_object, indent=4, ensure_ascii=False)

    return token

if __name__ == "__main__":
    print("Hello Word!")





