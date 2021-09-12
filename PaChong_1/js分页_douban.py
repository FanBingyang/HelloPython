
# 需要配置 webdriver.PhantomJS的环境变量

# 导入webdriver API对象，可以调用浏览器和操作页面
from selenium import webdriver
# 导入Keys，可以使用操作键盘，标签，鼠标
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
# 导入测试库
import unittest

class douyu(unittest.TestCase):
    # 初始化方法，必须是setUp()
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.num = 0
        self.count = 0

    # 测试方法必须要有test字样开头
    def testDouyu(self):
        self.driver.get("https://www.douyu.com/directory/all")
        while True:
            soup = bs(self.driver.page_source,"lxml")
            # 房间名,find_all返回列表
            names = soup.find_all("h3",{"class":"ellipsis"})

            # 观看人数，find_all返回列表
            numbers = soup.find_all("sapn",{"class":"dy-num fr"})

            # zip(names,numbers)将name和number着两个列表合并为一个元组：[(1,2),(3,4)]
            for name,number in zip(names,numbers):
                print(u"房间名："+name.get_text().strip()+"\t"+u"观看人数"+number.get_text().strip())
                self.num += 1
                # self.count += int(number.get_text().strip()) # 里面有些有汉字，所以不能直接转

            # 如果在页面源码里找到"下一页"为隐藏的标签，就退出循环
            if self.driver.page_source.find("shark-pager-disable-next") != -1:
                break

            # 通过class_name找到"下一页"元素并且一直点击
            self.driver.page_source.find_element_by_class_name("shark-pager-next").click()



    # 测试方法结束执行的方法
    def tearDown(self):

        print("当前网站直播人数:" + str(self.num))
        # print("当前网站观看人数:" + str(self.count))

        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    # 启动测试模块
    unittest.main()


