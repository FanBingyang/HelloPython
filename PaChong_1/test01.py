import urllib.request

# 构建一个自己的请求消息头,爬虫发爬虫第一步斗争
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}

# 通过urllib.request.Request()方法构建一个请求对象
request = urllib.request.Request("http://www.baidu.com",headers=headers)

# 向指定url地址发送请求，并返回服务器相应的类文件对象
response = urllib.request.urlopen(request)

# 服务器返回的类文件对象支持python文件对象的操作方法
# read()方法就是读取文件里的全部内容,返回字符串
html = response.read()

# 返回http的响应码,
print(response.getcode())

# 返回实际数据的实际url,防止重定向
print(response.geturl())

# 返回服务器响应的合同HTTP报头
print(response.info())

print(html)