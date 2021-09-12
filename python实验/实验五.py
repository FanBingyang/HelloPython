import re
import csv
import os

"""
    创建一个txt文件,写入文件，再次读取出来
"""
def creat():
    # 创建文件，操作为写入
    file = open('test.txt','w')
    # 写入内容
    file.write("学生姓名:fby\n")
    file.write("学生性别:男\n")
    file.write("学生年龄:20\n")
    file.write("联系电话:12345678910\n")
    # 关闭文件
    file.close()
    # 再次打开文件
    file = open('test.txt')
    # 读取文件内容
    print("test.txt文件内容如下:")
    print(file.read())
    file.close()

"""
    读取文件，统计文件内容的行数及单词的个数
"""
def count():
    # 读取文件
    file = open('zen.txt')
    word = 0        # 单词个数计数器
    row = 0         # 行数计数器
    # 统计行数，两种方法都可以
    # row = sum(1 for line in file)
    rex = r'\b(\w+)\b'
    for line in file:
        row += 1
        # 通过正则表达式匹配每一行的所有单词，匹配结果是列表，然后取出列表长度即可
        word += len(re.findall(rex,line))
    # 将文件指针移动到文件头
    file.seek(0)
    print("文本内容为:\n"+file.read())
    print("文本中的单词数为:{}\n文本的行数为:{}".format(word,row))
    file.close()

"""
    读取csv文件，对其进行指定操作
"""
def readCSV():
    file = open('score.csv','r')
    # 读取csv文件，接收一个可迭代的对象（比如csv文件），能返回一个生成器
    reader = csv.reader(file)
    # 解析出读取到的csv文件内容
    # rows = [row for row in reader]
    for i in range(1,4):
        # 每读取一次都要将文件指针移动到开始位
        file.seek(0)
        # 从csv文件读取第i列的数据
        column = [row[i] for row in reader]
        # 弹出第一个元素(科目名称)
        title = column.pop(0)
        # 总分计数
        mark = 0;
        # 循环对各个分数求和
        for score in column:
            mark += int(score)
        # 格式化输出,   {:.2f}是保留两位小数,   mark/len(column)总分除以个数
        print("{}:\t平均分:{:.2f}\t最高分:{}\t最低分:{}".format(title,mark/len(column),max(column),min(column)))
    file.close()

"""
    用户输入一个目录和文件名，搜索该目录及其子目录中是否存在该文件。
"""
def isHave(path,filename):
    # 对输入的目录路径进行遍历
    for dir in os.listdir(path):
        # 判断　父目录\子目录\文件　是否存在
        if os.path.exists(path+"\\"+dir+"\\"+filename):
            print("文件：{}存在于目录{}\{}\{}".format(filename,path,dir,filename))
            return path+"\\"+dir+"\\"+filename
        # 不存在，判断当前是否是目录，是那就进行递归遍历
        elif os.path.isdir(path+"\\"+dir):
            isHave(path+"\\"+dir,filename)


if __name__=="__main__":
    # creat()

    # count()

    # readCSV()

    isHave(path = input("输入一个目录路径:"),filename = input("输入一个文件名称:"))