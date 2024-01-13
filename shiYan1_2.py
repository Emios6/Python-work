# 输入三角形的边长和夹角，输出面积
import math
a = int(input("请输入三角形的一个边长："))
b = int(input("请输入三角形的另一个一个边长："))
angle = int(input("请输入三角形两边的夹角："))

area = 1/2*a*b * math.sin(angle * math.pi/180)
print("三角形的面积是：%.2f " % area)
