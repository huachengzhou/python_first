

import  os

import  time

# 返回当前工作目录
print(os.getcwd())

# 返回 path 的绝对路径
print(os.path.abspath(os.getcwd()))

dir1x = os.getcwd() + "\\"+str(int(time.time()))

# 创建目录
os.mkdir(dir1x)
print(dir1x)

os.chdir(dir1x)
print("新目录",os.getcwd())

