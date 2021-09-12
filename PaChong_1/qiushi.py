#
#

import urllib.request
from lxml import etree
import json

url = "https://www.qiushibaike.com/text/page/2/"
headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

request = urllib.request.Request(url,headers=headers)

html = urllib.request.urlopen(request).read()

# 响应返回的是字符串，加息为HTML DOM模式
text = etree.HTML(html)

# 返回所有段子的节点位置，contains()模糊查询方法，第一个参数是要匹配的标签，第二个参数是标签名部分内容
node_list = text.xpath('//div[contains(@id, "qiushi_tag")]')

items = {}
for node in node_list:
    # 取出用户名
    username = node.xpath('./div/a/h2')[0].text
    # 取出标签下的段子内容
    content = node.xpath('.//div[@class="content"]/span')[0].text
    # 取出标签里的点赞次数
    zan = node.xpath('./div[@class="stats"]//i')[0].text
    # 取出标签里的评论次数
    pinglun = node.xpath('./div[@class="stats"]//i')[1].text

    items = {
        "username":username,
        "content":content,
        "zan":zan,
        "pinglun":pinglun
    }

    print(items)

    with open("qiushidunazi.json","a") as f:
        array = json.dumps(items,ensure_ascii=False)
        f.write(array.encode("utf-8").decode()+"\n")
