"""
代理和web客户端授权验证处理器的使用
"""
import urllib.request
# 授权代理的用户名,密码,IP
test = "test"
password = "123456"
webserver = "10.85.16.12"

# 构建一个密码管理对象,可以用来保存和HTTP请求相关的授权账户信息
passwordMgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# 添加授权账户信息,第一个参数是realm如果没有指定就写None,后三个分别是站点IP,账户和密码
passwordMgr.add_password(None,webserver,test,password)
# HTTPBasicAutnHandler() HTTP基础验证处理器类
httpauth_handler = urllib.request.HTTPBasicAuthHandler(passwordMgr)
# 构建自定义open
opener = urllib.request.build_opener(httpauth_handler)

request = urllib.request.Request("http://"+webserver+"/")
# 没有授权验证信息
# response = urllib.request.urlopen(request)
# 有授权验证信息
response = opener.open(request)

print(response)