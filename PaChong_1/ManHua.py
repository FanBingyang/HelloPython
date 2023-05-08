# 从快看上爬取漫画《我不喜欢这世界，我只喜欢你》
# 2018-12-16
#


import urllib.request
from urllib.parse import urlencode
from lxml import etree
import os
from os import listdir
from PIL import Image
import shutil


# 定义全局变量，临时文件夹路径
PATH = "G:\\temp\\"
# 定义全局变量，最终漫画保存的路径
SAVE_PATH = "G:\\漫画\\test\\"

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
    # xpath定位全部章节链接元素
    x_path = "//div/div//table/tbody/tr/td[@class='tit']/a"
    # x_path = "//div/div//table/tbody/tr[1]/td[@class='tit']/a"  取页面上最上面刚更新的链接
    # 拿到链接的title，也就是章节的名字，用来当作文件名进行保存文件
    zhangjie_list = content.xpath(x_path+"/@title")
    # 返回所有匹配成功的章节链接的列表集合
    link_list = content.xpath(x_path+"/@href")
    # print(link_list)
    for link,name in zip(link_list,zhangjie_list):
        # 组合为每话漫画的链接
        fulllink = "https://www.kuaikanmanhua.com" + link
        # 下载漫画
        loadImage(fulllink,name)

    # 删除临时零碎漫画文件
    for fn in listdir(PATH):
        if fn.endswith('.jpg'):
            os.remove(PATH + fn)
    # 截取目录，输出结果为G:\temp
    p = PATH[:-1]
    # 删除临时文件夹
    os.rmdir(p)
    print("本次下载结束，临时文件已经删除！")


def loadImage(link,filename):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    request = urllib.request.Request(link, headers=headers)
    html = urllib.request.urlopen(request).read()
    # 解析
    content = etree.HTML(html)
    # 取出漫画片段链接的集合
    link_list = content.xpath("//div/div/div[@class='list comic-imgs']/img/@data-src")

    # 取出每个图片的连接以及定义漫画片段临时名称便于拼接
    for i,link in zip(range(1,len(link_list)+1),link_list):
        # 下载漫画片段到临时文件夹"G:\\temp\\"
        writeImage(link,"0000"+str(i))

    # 取到临时文件夹下的所有片段文件
    fillist = os.listdir(PATH)
    # 对取到的临时文件进行文件名排序，以便于后续拼接顺序正常，-4是截止到文件类型
    fillist.sort(key=lambda x:int(x[:-4]))
    # 获取当前文件夹中所有的jpg图像文件，并且用Image.open()打开保存在ims列表里，
    ims = [Image.open(PATH + fn) for fn in fillist if fn.endswith('.jpg')]
    # 获取第一张片段漫画的宽和高
    width,height = ims[0].size
    # 创建空白长图片
    result = Image.new(ims[0].mode,(width,height*len(ims)))
    # 进行拼接
    for i,im in enumerate(ims):
        result.paste(im,box=(0,i*height))
    # 保存拼接好的漫画
    result.save(SAVE_PATH+filename+".jpg")

    print("已经成功下载 《"+filename+"》")

def writeImage(link,filename):
    """
        作用：将图片内容写入到本地
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
        img = urllib.request.urlopen(request).read()
    except Exception:
        pass

    # 判断PATH临时文件夹是否存在，如果不存在则创建
    if os.path.exists(PATH) is False:
        os.makedirs(PATH)

    # 写入到本地磁盘文件内
    with open(PATH + filename + ".jpg", "wb") as f:
        f.write(img)

if __name__ == "__main__":
    # 快看漫画《我不喜欢这世界，我只喜欢你》
    url = "https://www.kuaikanmanhua.com/web/topic/2390/"
    loadPage(url)
