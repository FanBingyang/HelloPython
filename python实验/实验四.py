import re

""""
    将文本中重复连续重复两次的单词只保留一个
"""
def cnki():
    # 山河无恙，国富民强，这盛世，如你所愿。
    str = "The mountains mountains and rivers are are safe, \n" \
          "the country is rich rich and the people are strong strong.\n" \
          "This is a prosperous prosperous age, as you you wish."
    # 将字符串进行切割，返回列表
    str = str.split()
    # 定义空列表
    data = []
    # 循环遍历列表
    for i in range(len(str)):
        # 如果当前元素和前一个不同，添加进新列表
        if str[i] != str[i-1]:
            data.append(str[i])
    # 将列表转换成字符串进行打印
    print("原文本:"," ".join(str))
    print("新文本:"," ".join(data))

"""
    用户输入一段英文，然后输出这段英文中所有长度为3个字母的单词。
"""
def find():
    str = input("输入一段英文:")
    # \b 匹配一个单词边界，也就是指单词和空格间的位置
    pattern = re.compile(r'\b([a-zA-Z]{3})\b')
    list = pattern.findall(str)
    print("其中长度为3的单词有",list)

"""
    使用正则表达式清除字符串中的HTML标记
"""
def clear():
    html = '''<ul id="TopNav"><li><a href="/EditPosts.aspx" id="TabPosts">随笔</a></li>
    <li><a href="/EditArticles.aspx" id="TabArticles">文章</a></li>
    <li><a href="/EditDiary.aspx" id="TabDiary">日记</a></li>
    <li><a href="/Feedback.aspx" id="TabFeedback">评论</a></li>
    <li><a href="/EditLinks.aspx" id="TabLinks">链接</a></li>
    <li id="GalleryTab"><a href="/EditGalleries.aspx" id="TabGalleries">相册</a></li>
    <li id="FilesTab"><a href="Files.aspx" id="TabFiles">文件</a></li>
    <li><a href="/Configure.aspx" id="TabConfigure">设置</a></li>
    <li><a href="/Preferences.aspx" id="TabPreferences">选项</a></li></ul>'''

    html = re.sub(r"<.*?>",'',html)
    html = re.sub(r'\n','',html)
    print("清楚标记之后文本：\n",html)


"""
    有一段英文，其中有单独的字母I误写为i，编写程序进行纠正
"""
def correct():
    str = "i love you, my motherland, and i sincerely wish you more and more prosperity"

    s = re.sub(r"\bi\b","I",str)

    print("原文本:",str,"\n纠正之后的文本:",s)




if __name__=="__main__":

    # cnki()

    # find()

    correct()

    # clear()