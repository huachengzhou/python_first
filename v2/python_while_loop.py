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


