import urllib
from urllib.parse import urlencode
import urllib.request

url = "http://www.baidu.com/s"
headers = {"User-Agent":"Mozilla..."}
keyword = input("请输入需要查询的字符串:")

wd = {"wd":keyword}
# 通过urllib.parse.urlencode() 参数是一个字典类型
wd = urllib.parse.urlencode(wd)
# 拼接完整的url字符串
fullurl = url + "?" + wd
# 构造请求对象
request = urllib.request.Request(fullurl,headers = headers)
response = urllib.request.urlopen(request)

print(response.read())