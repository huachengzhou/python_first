import sys
import  os
import  pathlib



print(os.getcwd())
print(pathlib.Path.cwd())
print(os.pardir)

# pathTo = Path(os.getcwd())

# 获取父路径
# print(pathTo.parent)

print(os.path.dirname(os.path.dirname(os.getcwd())))
print(os.path.dirname(os.getcwd()))


print(os.path.join(os.path.dirname(os.getcwd()), '路径拼接', '真麻烦'))  # D:\pythonProjects\t2\路径拼接\真麻烦
paths = ('路径拼接', '真麻烦')
print(pathlib.Path.cwd().parent.joinpath(*paths))  # /Users/路径拼接/真麻烦