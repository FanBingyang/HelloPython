# 爬取百度贴吧美女吧上图片测试
# 2018-12-13
# fby

import urllib.request
from urllib.parse import urlencode
from lxml import etree

def loadPage(url):
    """
        作用:根据url发送请求,获取服务器相应的文件
        :param url:需要爬取的url地址
    """

    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
    request = urllib.request.Request(url)
    html = urllib.request.urlopen(request).read().decode("utf8")
    # 解析HTML文档为xml Dom模型
    content = etree.HTML(html)
    # 返回所有匹配成功的列表集合
    link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
    # print(link_list)
    # link_list = content.xpath('//a[@class="j_th_tit"]/@href')
    for link in link_list:
        fulllink = "http://tieba.baidu.com" + link
        # 组合为每个帖子的链接
        # print(link)
        loadImage(fulllink)

def loadImage(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    request = urllib.request.Request(link, headers=headers)
    html = urllib.request.urlopen(request).read()
    # 解析
    content = etree.HTML(html)
    # 取出帖子里每层层主发送的图片连接集合
    link_list = content.xpath('//div[@class="d_post_content j_d_post_content "]/img/@src')
    # 取出每个图片的连接
    for link in link_list:
        # print(link)
        writeImage(link)

def writeImage(link):
    """
        作用：将html内容写入到本地
        link：图片连接
    """
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    # 文件写入
    try:
        request = urllib.request.Request(link, headers = headers)
    except Exception as e:
        pass
    # 图片原始数据
    try:
        image = urllib.request.urlopen(request).read()
    except Exception:
        pass
    # 取出连接后10位做为文件名
    filename = link[-10:]
    # 写入到本地磁盘文件内
    with open(filename, "wb") as f:
        f.write(image)
    print("已经成功下载 "+ filename)

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
        fullurl = url + "&pn="+ str(pn)
        # print(fullurl)
        loadPage(fullurl)
    print("本次爬取结束,谢谢使用!")


if __name__ == "__main__":
    kw = input("请输入要爬取贴吧的贴吧名:")
    beginPage = int(input("请输入起始页:"))
    endPage = int(input("请输入结束页:"))

    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw":kw})
    fullurl = url+key
    tiebaSpider(fullurl,beginPage,endPage)
