import random

class Person:
    hand = ""
    footer = ""
    head = ""

# 这里是继承 Person
class Teacher(Person) :
    # 静态类变量
    empCount = 0

    def __init__(self,name,position):
        self.name = name
        self.position = position


    def print(self):
        print("名字:",self.name,"  职位:",self.position)
        print("__dict__ ",Teacher.__dict__ ,sep=":")
        print("__doc__",Teacher.__doc__,sep=":")
        print("__name__",Teacher.__name__,sep=":")
        print("__module__",Teacher.__module__,sep=":")
        print("__bases__ ",Teacher.__bases__ ,sep=":")


t1 = Teacher('张老师','数学')
t1.print()


t2 = Teacher('李老师','英语')
t2.print()
