

for x in range(1,10):
    for y in range(1,x+1):
        print(y,"x",x,"=",x*y,"   ",end="")
    print("\n")

if __name__ == '__main__':
    print("乘法表")