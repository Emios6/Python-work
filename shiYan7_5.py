# 第五题

dic_student = {}
print("请输入信息，输入！时输入结束。")
while True:
    a1 = input("请输入班级：")
    if a1 == '!':
        break
    a2 = input("请输入姓名：")
    a3 = input("请输入年龄：")
    a4 = input("请输入身高：")
    a5 = input("请输入体重：")
    dic_student[(a1, a2)] = [a3, a4, a5]

for i in dic_student:
    print(f"{i[0]}班", end="\t")
    print(i[1], end="\t")
    print(dic_student[i][0], end="\t")
    print(f"{dic_student[i][1]}cm", end="\t")
    print(f"{dic_student[i][2]}kg", end="\t")
    print("\n")
