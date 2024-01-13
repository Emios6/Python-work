# 利用递归法求最大公约数
def fun1(x, y):
    a1 = x % y
    if a1 == 0:
        return y
    else:
        return fun1(y, a1)


# 求最小公倍数
def fun2(x, y):
    return x * y / fun1(x, y)


# 接收数据
x = eval(input("请输入第一个数："))
y = eval(input("请输入第二个数："))

# 函数调用
a2 = fun1(x, y)
a3 = fun2(x, y)

print(f"最大公约数是：{a2}")
print(f"最小公倍数是：{a3}")
