#三角形
import math

a = eval(input("请输入三角形的边长a："))
b = eval(input("请输入三角形的边长b："))
c = eval(input("请输入三角形的边长c："))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        cir = a + b + c
        h = cir/2
        s = math.sqrt(h*(h-a)*(h-b)*(h-c))
        print("三角形的周长是：%.1f,三角形的面积是：%.1f"%(cir,s))
    else:
        print("输入的三边无法构成三角形！")
else:
    print("输入的三边无法构成三角形！")

