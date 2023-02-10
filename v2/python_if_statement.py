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
