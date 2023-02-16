import random


class Employee:
    # 所有员工的基类 empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享
    empCount = 0

    # 类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee", Employee.empCount, sep="  _")

    def displayEmployee(self):
        print("name:", self.name, " ;", "salary:", self.salary)

# 定义实例 1
t1 = Employee("张三", random.random() * random.random() * 10000)
t1.displayCount()
t1.displayEmployee()

# 定义实例 2
t2 = Employee("李四", random.random() * random.random() * 10000)
t2.displayCount()
t2.displayEmployee()
