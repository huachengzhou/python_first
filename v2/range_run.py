arr0 = range(10)

for kk in arr0:
    print(kk)

print("--------------------------")

arr1 = range(2, 7)

for i in arr1:
    print(i)

print("..............................")

arr2 = range(20, 100, 10)
for k in arr2:
    print(k)
    print('k', k)


def my_len(string):
    count_ = 0
    for x in string:
        count_ += 1
    return count_


print(my_len('sdhsdhhsdh'))


# 检查年龄
def checkAge(age):
    if age > 60:
        return '老年'
    elif age <= 60 & age > 40:
        return '中年'
    else:
        return None


print(checkAge(23))