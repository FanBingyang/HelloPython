#
#

import urllib.request
# json解析库，对应带lxml
import json
# json的解析语法，对应到xpath
import jsonpath

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
# print(response.read().decode())

# 取出json文件里的内容，返回格式是字符串
html = response.read().decode()
# 把json形式的字符串转换成python形式的Unicode字符串
unicodestr = json.loads(html)
# 取出json中的name对应的数据，p'y城市名
city_list = jsonpath.jsonpath(unicodestr,"$..name")
# 循环打印取出的数据
# for item in city_list:
#     print(item)

# dumps()默认中文为ASCII编码格式，ensure_ascii默认是Ture
# 加上参数ensure_ascii=False，返回的是Unicode字符串,方便使用，不加上参数返回的是ASCII编码形式，禁用ASCII编码格式
array = json.dumps(city_list,ensure_ascii=False)

with open("lagouCity.json","w") as f:
    f.write(array.encode("utf-8").decode()) # 将Unicode格式的array转换成utf-8格式写入文件，decode()是将byte转成str
