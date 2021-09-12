
"""
    将两个列表合并为一个字典
"""
def mergeList():
    a=['key1','key2','key3','key4','key5']
    b=['value1','value2','value3','value4','value5']

    print("列表a=",a,"\n列表b=",b)
    print("合并为字典：",dict(map(lambda x,y:[x,y],a,b)))

"""
    根据输入的键输出对应的值
"""
def findKey():
    dic = {"a":"A","b":"B",'c':'C'}
    temp = input("输入一个字母键:")
    result = dic.get(temp)
    if result==None:
        print("您输入的键不存在！")
    else:
        print("对应的键值为:{}".format(dic.get(temp)))

"""
    输入一个数字，输出百位以上的数字
"""
def hundred():
    temp = int(input("请输入一个三位以上的数字:"))
    if temp//100 == 0:
        print("输入有误!")
    else:
        print("百位以上的数字为:",temp//100)


"""
    将tuple(元组)转换成list(列表)
"""
def transform():
    s = (1,2,3)
    a = list(s)
    print("s=",s,"\na=",a)
    print("type(s):",type(s),"\ttype(a):",type(a))

if __name__=="__main__":
    # mergeList()

    # findKey()

    hundred()

    # transform()