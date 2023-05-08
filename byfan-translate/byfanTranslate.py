# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  byfanTranslate.py
@Desc   :  
@Author :  byfan
@Time   :  2022/10/11 16:51 
'''

import requests
from getToken import getToken


def translate(str):
    token = getToken()
    url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + token

    q = str  # example: hello
    # For list of language codes, please refer to `https://ai.baidu.com/ai-doc/MT/4kqryjku9#语种列表`
    from_lang = 'zh'  # example: en
    to_lang = 'en'  # example: zh

    # Build request
    headers = {'Content-Type': 'application/json'}
    payload = {'q': q, 'from': from_lang, 'to': to_lang}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    # print(result)
    # Show response
    # print(json.dumps(result, indent=4, ensure_ascii=False))

    translate_result = result['result']['trans_result'][0]['dst']
    return translate_result


if __name__ == "__main__":
    print("Hello Word!")
    translate("你好")
