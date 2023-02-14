
# python 学习笔记

+ 学习之前注意python版本区别,因为目前很多都是3.x版本了

+ 本学习笔记基于3.x+



## Python基础


### 输入和输出



#### 输出

+ Python print() 函数

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔
# sep -- 用来间隔多个对象，默认值是一个空格
# end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串
# file -- 要写入的文件对象
# flush -- 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新
# 返回值 无

```


+ 用print()在括号中加上字符串，就可以向屏幕上输出指定的文字


```python
print('hello world')
```

+ print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出

```python
print('漫','步','人','生')
```

+ print()也可以打印整数，或者计算结果

```python
print(12) 

print(12 + 20)
```

+ 设置间隔符

```python
print("美丽","人生",sep="-")
# 美丽-人生
```

+ 多行内容

```python


str = '''
ab
cd
'''

```


#### 输入

+ 用户从电脑输入一些字符 Python提供了一个input()，可以让用户输入字符串，并存放到一个变量里

```python
print("请输入你的名字!")
myName =input() 
print("你的名字是",myName,"!",sep="",end="")

#请输入你的名字!
#张三
#你的名字是张三!
```


### 数据类型和变量

+ 任何编程语言都需要处理数据，比如数字、字符串、字符等，我们可以直接使用数据，也可以将数据保存到变量中，方便以后使用
+ 变量（Variable）可以看成一个小箱子，专门用来“盛装”程序中的数据。每个变量都拥有独一无二的名字，通过变量的名字就能找到变量中的数据

+ 在编程语言中，将数据放入变量的过程叫做赋值（Assignment）。Python 使用等号=作为赋值运算符，具体格式为：

```python
name = 'value'
# name 表示变量名；value 表示值，也就是要存储的数据
```

+ 变量是标识符的一种，它的名字不能随便起，要遵守 Python 标识符命名规范，还要避免和 Python 内置函数以及 Python 保留字重名

```python
pi = 3.14
name = "blake" 
n = 20
n = 'dsdh'

```

+ 变量类型检测

```python
print(type('string'))
print(type(3.1415))
print(type(100))
print(type(''))

# <class 'str'>
# <class 'float'>
# <class 'int'>
# <class 'str'>

```


#### 基本类型

+ 布尔类型、整型、浮点型、字符串、列表、元组、集合、字典

```python
# 数值
digital_value = 0

# 字符串
str_value = "" 

# 列表
list_value = []

# 字典
ditc_value = {}

# 元组
tuple_value = ()

# Python中关于空类型的判断使用的内建函数any(),
```


```python
# 列表 也是数组 奇怪吧
list_value = [2,3,5]

print('length',len(list_value))


# 字典
ditc_value = {'a':'2'}

print("ditc_value",ditc_value)


# 元组 相当于常量
tuple_value = (2,'b')

print('tuple_value',tuple_value)
```


#### Python 运算符

```python
import random

# 简单运算符
a = 10 - 1
b = 11 * (2 + 5)
c = random.random() / 20
d = 20 % 4
# 这里是12的2次方
e = 12 ** 2
# 这里是9除以2 向下取整
f = 9 // 2

y1 = random.random() >= random.random()
y2 = random.random() == random.random()
y3 = random.random() <= random.random()

y4 = 2
y4 -= 1

y5 = 2
y5 += 1


print('a', '=', a)
print('b', '=', b)
print('c', '=', c)
print('d', '=', d)
print('e', '=', e)
print('f', '=', f)


print('y1', '=', y1)
print('y2', '=', y2)
print('y3', '=', y3)
print('y4', '=', y4)
print('y5', '=', y5)



```

#### 条件语句

```python
import random
# python 压根就不支持 switch
# python三元运算符  也是没有的
a1 = random.random()
a2 = random.random()

if (a1 >= a2):
    print("a1大于a2", a1, " ", a2)
    print("结束")

b1 = 12 + random.random()
b2 = 12 + random.random()

if (b1 == b2):
    print("b1==b2")
    print("比较结束")
elif (b1 < b2):
    print("b1<b2")
    print("比较结束")
else:
    print("不符合")
    print("比较结束")

```

#### 循环语句

```python
import random

for x in range(2, 10):
    print("x:", x)
    print(" ")

maxValue = 50

while (maxValue > 0):
    maxValue -= random.random()
    print("maxValue:", maxValue)
    print(" ")

minValue = 0

while (minValue < 100):
    minValue += random.random() * 10
    print("minValue:", minValue)
    print(" ")



for x in range(2,20):
    if(x % 2 == 0):
        print("偶数:",x)
    elif(x % 3 == 0):
        print("能被3整除:", x)
    else:
        print("临时变量:", x)



#
```

#### break 语句

```python


str1 = "人生五十年,如梦亦如幻。有生斯有死,壮士复何憾"

for x in str1:
    print("x:",x)
    if(x == ","):
        break




str2 = "Hubei couple opt for romantic, not lavish, wedding"

for y in str2:
    if(y == ' '):
        continue
    else:
        print(y)


#
```

#### pass 语句

Python pass 是空语句，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句。

```python
import random

index = 0
for i in range(2, int(random.random() * 100), 3):
    if (i % 2 >= 3):
        pass
    print(i)


pass
```


#### 字符串

字符串是 Python 中最常用的数据类型。我们可以使用引号 ( ' 或 " ) 来创建字符串。

```python


str1 = 'The Most Beautiful Swiss Books China Tour will be on exhibit in Shanghai from February 10 to 13 at Shanghai Ming Contemporary Art Museum'


print(str1)
print(str1[0])
print(str1[1])
print(max(str1))
print(min(str1))
print(str1.upper())

```


#### 列表(List)


```python
import random

# 自己定义一个字符串函数
def randomString():
    arr = []
    str_value = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;?@[\]^_`{|}~"
    len_value = len(str_value)
    for x in range(1,10):
        index = int(random.uniform(0,len_value))
        arr.append(str_value[index])
    return "-".join(arr)


arr1 = [int(random.random() * 10), int(random.random() * 10), int(random.random() * 10), int(random.random() * 10)]
print(arr1)

print(arr1[0])

print(arr1[1])

print("len",len(arr1))

arr1.reverse()
print(arr1)

arr1.sort()

print(arr1)

arr2 = []
arr3 = []

print(randomString())

for x in range(1,5):
    arr2.append(randomString())
    arr3.append(randomString())
    pass



print(arr2)
# 删除第一个元素
del arr2[0]
print(arr2)


arr2.insert(0,'a')
print(arr2)
arr2.pop(1)
print(arr2)
arr2.remove("a")
print(arr2)
```


####  函数

```python
# 打印一下
def printNew(temp):
    print(temp)
    pass


# 加法
def add(a, b):
    return a + b


# 减法
def sub(x, y):
    return x - y


# 除法
def div(x, y):
    return x / y


# 取模
def takingMold(m, n):
    return m % n


# 次方
def runPower(m, n):
    return m ** n


a = runPower(2, 3)

print(a)

```


#### 元组

+ Python 的元组与列表类似，不同之处在于元组的元素不能修改
+ 元组使用小括号，列表使用方括号

```python


tup1 = (1,3)
tup2 = ('abc', 'xyz')

print(tup1[0])
print(tup1[1])

# 以下修改元组元素操作是非法的
# tup1[0] = 100

# 元组 不能修改但是可以组合


# 但我们可以对元组进行连接组合

# 创建一个新的元组
tup3 = tup1 + tup2

print(tup3)
```

####  字典(Dictionary)

字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值 key:value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 ,格式如下所示：

```python
d = {key1 : value1, key2 : value2 }
```



### 重要函数

#### range

range()的三种创建方式：

第一种：只有一个参数（小括号中只给了一个数）即range(stop) 

第二种：range(start,stop) （给了两个参数，即小括号中给了两个数）

第三种：range(start,stop,step)：创建一个在[start,stop)之间，步长为step;

```python
arr0 = range(10)

for kk in arr0:
    print(kk)

print("--------------------------")

arr1 = range(2, 7)

for i in arr1:
    print(i)

print("..............................")

arr2 = range(20, 100, 10)
for k in arr2:
    print(k)

```

## 模块

> Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句

+ mathModule.py

```python
import random


# 随机整数
def randomInt():
    temp = int(random.random() * 1000)
    temp += int(random.uniform(0, 100))
    return temp


# 随机浮点数
def randomFloat():
    temp = 0
    temp += random.random() * 10
    temp *= random.random()
    return temp


# 获取单独一个asii 字符
def getOneChar():
    # 小写字母a-z：97-122
    arr1 = range(97, 122)
    # 大写字母A-Z：65-90
    arr2 = range(65, 90)
    # 数字0-9：48-57
    arr3 = range(48, 57)
    arr0 = []
    arr0.extend(arr1)
    arr0.extend(arr2)
    arr0.extend(arr3)
    index = int(random.uniform(0, len(arr0)))
    tempNumber = arr0[index]
    return chr(tempNumber)


# 获取随机字符串
def randomString(tempLen):
    temp = ""
    for x in range(1, tempLen):
        temp += getOneChar()
    return temp


```

```python
import mathModule
# 只有同级目录才能这样

print(mathModule.randomInt())
print(mathModule.randomFloat())
print(mathModule.getOneChar())
print(mathModule.randomString(92))
```

+ 导入非本级模块

```python
import sys


sys.path.append("D:\\pythonProjects\\t2\\gg")

import newmodule

print(sys)
newmodule.newPrint('sdhsdhsh')
```

or 

```python
import sys
import  os

#父路径
str1 = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
#再次取父路径
str1 = os.path.abspath(os.path.join(str1, os.pardir))
sys.path.append(str1+"\\gg")

import newmodule


newmodule.newPrint('kkkk')
```


## 文件

+ open()

open() 函数用于创建或打开指定文件，该函数的常用语法格式如下：

```
file = open(file_name [, mode='r' [ , buffering=-1 [ , encoding = None ]]])
```

此格式中，用 [] 括起来的部分为可选参数，即可以使用也可以省略。其中，各个参数所代表的含义如下：

+ file：表示要创建的文件对象。
+ file_name：要创建或打开文件的文件名称，该名称要用引号（单引号或双引号都可以）括起来。需要注意的是，如果要打开的文件和当前执行的代码文件位于同一目录，则直接写文件名即可；否则，此参数需要指定打开文件所在的完整路径。
+ mode：可选参数，用于指定文件的打开模式。可选的打开模式如表 1 所示。如果不写，则默认以只读（r）模式打开文件。
+ buffering：可选参数，用于指定对文件做读写操作时，是否使用缓冲区（本节后续会详细介绍）。
+ encoding：手动设定打开文件时所使用的编码格式，不同平台的 ecoding 参数值也不同，以 Windows 为例，其默认为 cp936（实际上就是 GBK 编码）。

+ open 函数支持的文件打开模式

| 模式 | 意义 | 注意事项 |
| --- | --- | --- |
| r | 只读模式打开文件，读文件内容的指针会放在文件的开头。 | 操作的文件必须存在。 |
| rb | 以二进制格式、采用只读模式打开文件，读文件内容的指针位于文件的开头，一般用于非文本文件，如图片文件、音频文件等。 |
| r+ | 打开文件后，既可以从头读取文件内容，也可以从开头向文件中写入新的内容，写入的新内容会覆盖文件中等长度的原有内容。 |
| rb+ | 以二进制格式、采用读写模式打开文件，读写文件的指针会放在文件的开头，通常针对非文本文件（如音频文件）。 |
| w | 以只写模式打开文件，若该文件存在，打开时会清空文件中原有的内容。 | 若文件存在，会清空其原有内容（覆盖文件）；反之，则创建新文件。 |
| wb | 以二进制格式、只写模式打开文件，一般用于非文本文件（如音频文件） |
| w+ | 打开文件后，会对原有内容进行清空，并对该文件有读写权限。 |
| wb+ | 以二进制格式、读写模式打开文件，一般用于非文本文件 |
| a | 以追加模式打开一个文件，对文件只有写入权限，如果文件已经存在，文件指针将放在文件的末尾（即新写入内容会位于已有内容之后）；反之，则会创建新文件。 |   |
| ab | 以二进制格式打开文件，并采用追加模式，对文件只有写权限。如果该文件已存在，文件指针位于文件末尾（新写入文件会位于已有内容之后）；反之，则创建新文件。 |   |
| a+ | 以读写模式打开文件；如果文件存在，文件指针放在文件的末尾（新写入文件会位于已有内容之后）；反之，则创建新文件。 |   |
| ab+ | 以二进制模式打开文件，并采用追加模式，对文件具有读写权限，如果文件存在，则文件指针位于文件的末尾（新写入文件会位于已有内容之后）；反之，则创建新文件。 |   |


+ File对象的属性

| 属性 | 描述 |
| --- | --- |
| file.closed | 返回true如果文件已被关闭，否则返回false。 |
| file.mode | 返回被打开文件的访问模式。 |
| file.name | 返回文件的名称。 |
| file.softspace | 如果用print输出后，必须跟一个空格符，则返回false。否则返回true。 |


+ 如下实例：

```python
def fileF4(dir):
    f1 = open(dir, "r+", encoding="UTF-8")
    print("文件名: ", f1.name)
    print("是否已关闭: ", f1.closed)
    print("访问模式: ", f1.mode)
fileF4("D:\\pythonProjects\\t2\\readme.md")
```

+ open() 使用的一些例子

```python
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
```

[参考1](https://www.runoob.com/python/python-numbers.html)
[参考2](http://c.biancheng.net/view/2171.html)
[参考3](https://www.liaoxuefeng.com/wiki/1016959663602400/1017106984190464)
[参考4](https://docs.pythontab.com/)


