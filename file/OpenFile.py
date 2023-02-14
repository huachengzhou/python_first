import os
import random
import time

dir1 = "D:\\pythonProjects\\t2\\打包编辑器安装.md"


def fileF1(dir):
    f1 = open(dir, "r", encoding="UTF-8")

    # 读取
    # file 表示已打开的文件对象；size 作为一个可选参数，用于指定一次最多可读取的字符（字节）个数，如果省略，则默认一次性读取所有内容
    # print(f1.read())
    print(f1.read(20))

    # 关闭文件
    f1.close()


def fileF2(dir):
    f1 = open(dir, "r+", encoding="UTF-8")
    # file 为打开的文件对象；size 为可选参数，用于指定读取每一行时，一次最多读取的字符（字节）数
    print(f1.readline())
    print(f1.readline(1))
    print(f1.readline(2))
    print(f1.readline(5))

    # 关闭文件
    f1.close()


def fileF3(dir):
    f1 = open(dir, "r+", encoding="UTF-8")
    # readlines() 函数用于读取文件中的所有行，它和调用不指定 size 参数的 read() 函数类似，只不过该函数返回是一个字符串列表，其中每个元素为文件中的一行内容。
    lines = f1.readlines()
    for str in lines:
        print(str)
    f1.close()


def fileF4(dir):
    f1 = open(dir, "r+", encoding="UTF-8")
    print("文件名: ", f1.name)
    print("是否已关闭: ", f1.closed)
    print("访问模式: ", f1.mode)


def fileF5():
    # write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
    # write()方法不会在字符串的结尾添加换行符('\n')：
    # 语法 fileObject.write(string)

    num1 = int(time.time())
    num2 = int(random.random() * 100 * random.random()) * int(random.random() * 100) + int(random.random() * 100 * random.random())
    str2 = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\file" + "\\" + str(num1) + ".txt"
    fo = open(str2, "w")
    fo.write(str(num2 + time.time()))
    fo.flush()
    fo.close()

def fileF6():
    strList = []
    for x in range(0,100):
        strList.append(str(time.time() * time.time()) + '\n' )
    str2 = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\file" + "\\" + str(float(time.time())) + "_writelines.txt"
    fo = open(str2, "w")
    # 写入函数只有 write() 和 writelines() 函数，而没有名为 writeline 的函数
    fo.writelines(strList)

    fo.flush()
    fo.close()

# fileF1(dir1)

# fileF2(dir1)

# fileF3(dir1)

# fileF4(dir1)

# fileF5()

fileF6()


