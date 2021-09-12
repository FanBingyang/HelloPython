
import re
import random
"""
    输入一个数a，在输入一个数n，求a+aa+aaa+a...a(n个a)之和
"""
def add():
    sum = 0;
    num = input("输入一个循环相加的数字:")
    n = int(input("输入循环的次数:"))
    for i in range(1,n+1):
        temp = int(i * num)
        sum += temp
        if i < 10:
            print(temp,'+ ', end = '')
    print(temp,'=',sum)

"""
    输入一串字符作为密码，密码只能由数字与字母组成,输出对应密码强度。
    密码强度判断准则如下（满足其中一条，密码强度增加一级）：
    1:有数字；2:有大写字母；3:有小写字母；4:位数不少于8位。
"""
def judge():
    str = input("输入一个只有数字和字母的密码:")
    level = 0       # 记录密码强度
    # 判断是否包含处数字和字母以外的字符
    if bool(re.search(r'[^0-9a-zA-Z]',str)):
        print("输入有误(包含其他字符)")
        return
    # 通过正则表达式的search()判断输入de字符串中是否含有数字
    if bool(re.search(r'\d', str)):
        level += 1
    # 判断是否含有大写字母
    if bool(re.search(r'[A-Z]',str)):
        level +=1
    # 判断是否含有小写字母
    if bool(re.search(r'[a-z]',str)):
        level +=1
    # 判断长度是否不小于8，即对所有字符匹配8次以上
    if bool(re.search(r'.{8,}',str)):
        level +=1
    print("你输入的密码等级为:",level)


"""
    返回该数的平方
"""
def lamdba(num):
    return num*num
"""
    计算一个列表中所有元素的平方之和
"""
def lamdbaSUM():
    sum = 0
    # 随机生成10个1~100之间的数存入列表
    list = random.choices(range(1,100),k=10)
    for i in list:
        sum += lamdba(i)
    print("生成的随机列表为:",list,"\n列表中各元素平方之和为:",sum)





if __name__=="__main__":

    # add()

    # judge()

    lamdbaSUM()