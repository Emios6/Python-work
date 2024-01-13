#将整数分解
def fun(x):
    #定义一个列表res用来存放分解出来的因数
    res = []
    yinShu = 2
    #进行拆分
    while x > 1:
        while x % yinShu == 0:
            res.append(yinShu)
            x = x // yinShu
        yinShu += 1
    return res

a = int(input("请输入一个整数："))
# 调用函数
res = fun(a)

# 输出
print(f"{a}=", end="")
for i in range(len(res)):
    if i != len(res) - 1:
        print(res[i], end="*")
    else:
        print(res[i])
