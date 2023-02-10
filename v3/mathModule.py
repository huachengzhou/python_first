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

