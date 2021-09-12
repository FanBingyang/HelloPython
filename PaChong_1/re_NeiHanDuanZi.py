import urllib.request
import re
import time

class Spider:
    def __init__(self):
        # 初始化起始页位置
        self.page = 2
        # 爬取开关,如果位True继续爬取
        self.switch = True


    def loadPage(self):
        """下载页面"""
        url = "http://www.neihan8.com/article/index_" + str(self.page) + ".html"

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}

        # 构建一个Handler处理器对象,参数是一个字典.包括代理类型和代理服务器IP+PROT
        httpproxy_handler = urllib.request.ProxyHandler({"http": "121.33.220.158:808"})
        # 构建一个没有代理的处理器对象
        nullproxy_handler = urllib.request.ProxyHandler({})
        opener = urllib.request.build_opener(httpproxy_handler)
        # 构建里一个全局的opener,之后所有的请求都可以用urlopen(0方式去发送,也附带Handler的功能
        urllib.request.install_opener(opener)

        requst = urllib.request.Request(url,headers=headers)
        response = urllib.request.urlopen(requst)

        # 获取每页的HTML源码
        print("正在下载数据...")
        html = response.read().decode('utf-8')
        # print(html)
        # 创建正则表达式规则对象 匹配每页的段子内容,re.S表示匹配全部字符串内容
        pattern = re.compile('<div\sclass="desc">(.*?)</div>',re.S)

        # 将正则匹配对象应用到html源码字符串里,返回这个页面所有的段子的列表
        content_list = pattern.findall(html)

        # 输出查看段子内容
        # for content in content_list:
        #     print(content)

        # 调用方法处理段子内容
        self.dealPage(content_list)


    def dealPage(self,content_list):
        """处理每一页的段子"""
        print("正在写入本地...")
        for content in content_list:
            # print(type(content))
            self.writePage(content)


    def writePage(self,content):
        """把每条段子逐格写入文件"""
        with open("duanzi.txt","a") as f:
            f.write(content+"\r\n")

    def startWork(self):
        """控制爬虫运行"""
        while self.switch:
            self.loadPage()
            flag = input("如果继续爬取,请按回车键(退出输入quit)")
            if flag == "quit":
                self.switch = False
            self.page += 1
        print("谢谢使用!")


if __name__ == "__main__":
    duanziSpider = Spider()
    duanziSpider.startWork()