def sumf(x, n):
    sum1 = 0
    for i in range(1, n+1):
        sum1 = sum1 + int(str(x) * i)
    print(f"结果是{sum1}")


sumf(2, 5)

