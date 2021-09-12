import urllib.request

# 构建一个HTTPHandler处理器,支持处理HTTP的请求
# http_handler = urllib.request.HTTPHandler()

# 在HTTPHandler增加参数"debuglevel=1"将会自动打开Debug log模式
# 程序在执行的时候会打印发包的信息
http_handler = urllib.request.HTTPHandler(debuglevel=1)


# 调用build_opener(0方法构建一个自定义的opener对象,参数是构建的处理器对象
opener = urllib.request.build_opener(http_handler)

request = urllib.request.Request("http://www.baidu.com/")

response = opener.open(request)

print(response.read().decode())