import random

"""生成1000个0~100以内的随机数，并统计每个元素出现的个数"""
def SuiJiShu():
    x = [random.randint(0,100) for i in range(1000)]
    y = set(x)   # 创建一个无序不重复元素集，删除重复元素
    for i in y:
        print("数字",i,"，出现次数：",x.count(i))

"""接收一个字符串，统计其中大写字母、小写字母、数字、其他字符的个数，并以元组的形式返回"""
def countStr(str):
    char_count = 0      # 统计小写字母
    CHAR_count = 0      # 统计大写字母
    int_count = 0       # 统计数字
    other_count = 0     # 统计其他字符

    for i in str:
        if i.isdigit():
            int_count += 1
        elif i.isupper():
            CHAR_count += 1
        elif i.islower():
            char_count += 1
        else:other_count += 1
    tup = (CHAR_count,char_count,int_count,other_count)
    return tup

"""读取文本文件data.txt中所有整数，将其排序后写入文本文件data_asc.txt中"""
def sortTXT():
    file = open("data.txt","r")
    data = file.readlines()         # 读出文本数据
    string = " ".join(data)         # 转换成字符串
    newData = string.split(",")     # 切割成列表
    newData = [int(i) for i in newData]     # 将列表数据转成int类型（因为如果不是int类型，sort()将按字符进行排序）
    newData.sort()                          # 对列表进行排序
    newData = [str(i)+' ' for i in newData] # 将列表数据转成str类型（因为文件写入需要是字符串）
    print(newData)
    with open("data_asc.txt","w") as f:
        f.writelines(newData)       # 进行数据写入

"""
对于一个十进制的正整数，定义f(n)为其各位数字的平方和，示例如下：
    f(13) = 1 ** 2 + 3 ** 2 = 10
    f(207) = 2 ** 2 + 0 ** 2 + 7 ** 2 = 53
下面给出三个正整数k, a, b,你需要计算有多少个正整数n满足a<=n<=b，且k*f(n)=n
    输入：第一行包含3个正整数k, a, b；k>=1，a，b<=10**18，a<=b；
    输出：输出对应的答案;
范例：
    输入：51 5000 10000
    输出：3
"""
def fn():
    sum = 0         # 统计个数
    shuru = input("请输入三个数字k、a、b：")
    data = shuru.split()                # 通过空格将输入的字符串分割
    data = [int(x) for x in data]       # 将数据转成int型
    n = data[1]                         # 保存数据a
    while n <= data[2]:                 # 循环a~b
        dd = str(n)                     # 将数据转成字符串用于分割
        dd = [int(x) for x in dd]       # 将数据按位分开并转成int型
        fn = 0
        for x in dd:
            fn += x*x                   # 计算fn
        if data[0]*fn == n:             # 计算并判断
            sum += 1                    # 如果存在个数加一
        n += 1
    print(sum)



if __name__=="__main__":

    # SuiJiShu()

    # print("字符串中的大写字母、小写字母、数字和其他字符的个数为：",countStr(input("请输入一个字符串:")))

    # sortTXT()

    fn()