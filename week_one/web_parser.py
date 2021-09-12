from bs4 import BeautifulSoup

info = []
# 打开本地网页
with open('D:\\HTML\\HTML工程\\HelloPaChong\\week_one\\html文件\\new_index.html','r') as web_data:
    soup = BeautifulSoup(web_data,'lxml') #解析网页
    # print(soup) #输出网页源码信息

    # 在浏览器中复制选中一个图片的位置，然后在这解析
    image = soup.select('body > div.main-content > ul > li:nth-of-type(1) > img')
    # print(image) #输出要解析的图片在网页中的代码
    #拿到网页中相同位置的图片
    images = soup.select('body > div.main-content > ul > li > img')
    # print(images)
    #拿到网页中的文本标题
    titles = soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    # print(titles)
    #循环拿出所有标题中的文本内容
    # for title in titles:
    #     print(title.get_text())

    # 拿到描述
    descs = soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    # 拿到评分
    rates = soup.select('body > div.main-content > ul > li > div.rate > span')
    # 拿到分类,因为分类又多个，是一对多的关系，所以要拿到父级元素
    cates = soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')


    #循环筛选出所有的图片和相对应的文本，然后存到一个字典里
    for title,desc,cate,rate,img in zip(titles,descs,cates,rates,images):
        data = {
            'title':title.get_text(),
            'desc':desc.get_text(),
            'cate':list(cate.stripped_strings),#用一个stripped_strings拿到父级元素下的所有元素内容，并保存在一个集合中
            'rate':rate.get_text(),
            'image':img.get('src') # 拿出标签中的一个属性
        }
        # print(data)
        info.append(data)#将所有数据放进列表中

# 通过循环遍历出评分大于3的文章
for i in info:
    if float(i['rate']) > 3:
        print(i['title'],i['cate'])

'''
body > div.main-content > ul > li:nth-child(1) > img
body > div.main-content > ul > li:nth-child(1) > div.article-info > h3 > a
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.description
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.meta-info > span:nth-child(2)
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.meta-info > span:nth-child(1)
body > div.main-content > ul > li:nth-child(1) > div.rate > span
'''







