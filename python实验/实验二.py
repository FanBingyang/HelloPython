import random

"""
    判断用户输入的字符是数字字符、字母字符还是其他字符
"""
def judge():
    temp = input("请输入一个字符：")
    if temp >='0' and temp <='9':
        print("你输入的是数字。")
    elif (temp >='a' and temp <='z') or (temp >='A' and temp <='Z'):
        print("你输入的是字母。")
    else:print("你输入的是其他字符。")

"""
    根据输入的点的横坐标和纵坐标，输出该点所在的象限。
"""
def xiangXian():
    x = int(input("请输入横坐标:"))
    y = int(input("请输入纵坐标:"))
    if x == 0 and y == 0:
        print("你输入的点({},{})在原点".format(x,y))
    elif x == 0:
        print("你输入的点({},{})在X轴".format(x,y))
    elif y == 0:
        print("你输入的点({},{})在Y轴".format(x,y))
    elif x > 0:
        if y>0:
            print("你输入的点({},{})在第一象限".format(x, y))
        else:
            print("你输入的点({},{})在第四象限".format(x,y))
    else:
        if y > 0:
            print("你输入的点({},{})在第二象限".format(x, y))
        else:
            print("你输入的点({},{})在第三象限".format(x, y))

"""
    产生两个0~100之间（包含0和100）的随机整数RND1和RND2，求这两个整数的最大公约数和最小公倍数
"""
def math():
    random1 = random.randint(0,100)
    random2 = random.randint(0,100)
    print("两个随机数分别为{}和{}".format(random1, random2))
    if random1 < random2:      # 判读两个整数的大小,目的为了将大的数作为除数,小的作为被除数
        random1,random2 = random2,random1   # 交换两个数的值

    vari1 = random1 * random2  # 计算出两个整数的乘积，方便后面计算最小公倍数
    vari2 = random1 % random2  # 先整除取余
    while vari2 != 0:      # 判断余数是否为0，不为0就继续运算
        random1 = random2
        random2 = vari2
        vari2 = random1 % random2

    vari1 = vari1 / random2   # 最小公倍数等于两个数的乘积除以最大公约数

    print("最大公约数为:{}".format(random2))
    print("最小公倍数为:{}".format(int(vari1)))

"""
    一球从100m高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，
    共经过多少米？第10次反弹多高？
"""
def ball():
    height = 100
    s = 0
    for i in range(1,11):
        s = s+height
        height = height/2
    print("第十次落地共经过{}米".format(s))
    print("第十次反弹{}米高".format(height))

if __name__=="__main__":
    # judge()

    # xiangXian()

    # math()

    ball()


