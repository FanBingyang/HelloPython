
"""
ajax方式加载的页面,数据来源一定的是json
"""

import urllib.request
from urllib.parse import urlencode

# 听过抓包获取url
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"


headers = {"User-Agent": "Mozilla/5.0(Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/70.0.3538.110 Safari/537.36"}
formdata = {
    "start":"0",
    "limit":"20",
}

# data = urllib.parse.urlencode(formdata).encode("utf-8")
data = bytes(urllib.parse.urlencode(formdata),encoding='utf-8')


request = urllib.request.Request(url,data = data,headers=headers)
print(urllib.request.urlopen(request).read().decode())
