

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

# os.chdir(dir1x)
# print("新目录",os.getcwd())


# 获取 path 路径的基本名称，即 path 末尾到最后一个斜杠的位置之间的字符串 如 readme.md
print(os.path.basename("D:\\pythonProjects\\t2\\readme.md"))

# 判断路径是否为文件
print(os.path.isfile("D:\\pythonProjects\\t2\\readme.md"))

# 判断路径是否为目录
print(os.path.isdir("D:\\pythonProjects\\t2"))