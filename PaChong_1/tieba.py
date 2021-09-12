import urllib.request
from urllib.parse import urlencode

def loadPage(url,filename):
    """
        作用:根据url发送请求,获取服务器相应的文件
        :param url:需要爬取的url地址
        :param filename:处理的文名
        :return:返回服务器响应的html文件
    """
    print("正在下载 "+filename +"...")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
    request = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(request).read().decode("utf8")
    # print(html)
    return html

def writePage(html,filename):
    """
        作用:将html文件写入到本地
    :param html: 服务器响应文件内容
    :return:
    """
    print("正在保存"+filename)
    # 文件写入本地
    with open(filename,"w",encoding="utf-8") as f:
        f.write(html)
    print("-" * 30)

def tiebaSpider(url,beginPage,endPage):
    """
        作用:贴吧爬虫调度器,负责组合处理每个页面的url
        url:贴吧url的前部分
        beginPage:起始页
        endPage结束页
    :return:
    """
    for page in range(beginPage,endPage+1):
        pn = (page - 1) * 50
        filename = "第"+str(page)+"页.html"
        fullurl = url + "&pn="+ str(pn)
        # print(fullurl)
        html = loadPage(fullurl,filename)
        # print(html)
        writePage(html,filename)
    print("本次爬取结束,谢谢使用!")


if __name__ == "__main__":
    kw = input("请输入要爬取贴吧的贴吧名:")
    beginPage = int(input("请输入起始页:"))
    endPage = int(input("请输入结束页:"))

    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw":kw})
    fullurl = url+key
    tiebaSpider(fullurl,beginPage,endPage)
