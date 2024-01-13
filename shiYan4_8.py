# 根据坐标输出所在象限

x = eval(input("请输入横坐标x："))
y = eval(input("请输入纵坐标y："))

if x > 0 and y > 0:
    print("该点在第一象限！")
elif x > 0 and y < 0:
    print("该点在第四象限！")
elif x > 0 and y == 0:
    print("该点在x轴的正方向上！")
elif x < 0 and y > 0:
    print("该点在第二象限！")
elif x < 0 and y < 0:
    print("该点在第三象限！")
elif x < 0 and y == 0:
    print("该点在x轴的负方向上！")
elif x == 0 and y > 0:
    print("该点在y轴的正方向上！")
elif x == 0 and y < 0:
    print("该点在y轴的负方向上！")
elif x == 0 and y == 0:
    print("该点在坐标轴原点！")