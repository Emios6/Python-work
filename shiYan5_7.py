

sum = 0
sum1 = 0
sum2 = 0
count = 0
while True:
    s = input("请输入数字（以A为结尾）：")
    if s == 'A':
        break
    else:
        count = count + 1
        n = eval(s)
        sum = sum + n
        if n % 2 ==0:
            sum1 =sum1 + n
        else :
            sum2 = sum2 + n

print(f"所有奇数和：{sum2}")
print(f"所有偶数和：{sum1}")
print(f"所有数的平均值：{sum/count}")