list1 = [18, 22, 35, 34, 51]
sum1 = 0
for i in list1:
    sum1 += (lambda x: x ** 2)(i)
print(sum1)