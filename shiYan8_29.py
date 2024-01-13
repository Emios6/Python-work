def fun(n):
    if n == 0:
        y = 0
    elif n == 1:
        y = 1
    elif n == 2:
        y = 2
    else:
        y = fun(n-1)+fun(n-2)+fun(n-3)
    return y


n = int(input("请输入一个正整数："))
print(fun(n))