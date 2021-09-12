import urllib
import urllib.request
import http.cookiejar as HC
from urllib.parse import urlencode

# 通过Cookiejar()类创建一个ciikieJar()对象,用力啊保存cookie的值
cookie = HC.CookieJar()
# 通过HTTPCookieProcessor()处理器类构建一个处理器对象,用来处理cookie
# 参数就是构建的CookieJar()对象
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

# 构建一个自定义的opener
opener = urllib.request.build_opener(cookie_handler)

# 自定义opener的addheaders的参数,可以赋值HTTP报头参数
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]

# renren网的登录接口
url = "http://www.renren.com/PLogin.do"

# 需要登录的账户密码
data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}

# 通过urlencode()编码转换
data = urllib.parse.urlencode(data).encode('utf-8')

# 第一次是post请求，发送登录需要的参数，获取cookie
request = urllib.request.Request(url,data=data )

# 发送第一次的post请求，生成登录后的cookie(如果登录成功的话)
response = opener.open(request)

print(response.read().decode())

# 第二次可以是get请求，这个请求将保存生成cookie一并发到web服务器，服务器会验证cookie通过
response_deng = opener.open("http://www.renren.com/410043129/profile")

# 获取登录后才能访问的页面信息
print(response_deng.read().decode())