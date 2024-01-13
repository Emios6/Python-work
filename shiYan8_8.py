def isNum(x):
    list1 = []
    for i in range(3, 8):
        k = x * i
        list1.append(str(k))

    list2 = []
    for j in range(len(list1)):
        sum1 = 0
        for i in range(len(list1[j])):
            sum1 += int(list1[j][i])
        list2.append(sum1)

    for i in range(len(list2)):
        if i != (len(list2) - 1):
            if list2[i] != list2[i + 1]:
                break
        else:
            if list2[i] != list2[i - 1]:
                break
    else:
        return 0

    return 1


count = 0
for i in range(100, 1000):
    if isNum(i) == 0:
        count += 1
        print(f"x={i}:x*3={i*3}, x*4={i*4}, x*5={i*5}, x*6={i*6}, x*7={i*7}", end="\n")
print(f"共有{count}个符合条件的三位数")

