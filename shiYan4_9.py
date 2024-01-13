# 划分等级

Score = eval(input("请输入分数（百分制）:"))

if Score >= 90:
    print("成绩等级为：优")
elif Score >= 80 and Score < 90:
    print("成绩等级为：良")
elif Score >= 70 and Score < 80:
    print("成绩等级为：中")
elif Score >= 60 and Score < 70:
    print("成绩等级为：及格")
elif Score < 60:
    print("成绩等级为：不及格")
