import os

import time

import random

str2 = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\file" + "\\" + "_writelines.txt"
strDir = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\file" + "\\" + str(random.random())
str21 = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\file" + "\\" + "_zzx.txt"
str3 = os.path.dirname(str2) + "\\_v0000.text"

os1 = open(str2, "w")
os2 = open(str21, "w")

strList = []
for x in range(0, 100):
    strList.append(str(time.time() * time.time()) + '\n')

os1.writelines(strList)
os1.flush()
os1.close()

os2.write(os.getcwd())
os2.flush()
os2.close()



print(str3)
print(str2)
# 重命名
os.rename(str2, str3)


print(str21)

# 删除文件
os.remove(str21)

os.mkdir(strDir)
print(strDir)

# 删除文件夹
os.rmdir(strDir)