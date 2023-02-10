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