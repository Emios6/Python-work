lst_student = [["001", "李梅", 19], ["002", "刘祥", 20], ["003", "张武", 18]]
lst_student.append(["004", "刘宁", 20])
lst_student.append(["006", "梁峰", 19])
lst_student.insert(4, ["005", "张歌", 20])
x1 = lst_student.index(["003", "张武", 18])
print(f"学号{lst_student[x1][0]},姓名{lst_student[x1][1]},年龄{lst_student[x1][2]}")
print(
    f"{lst_student[0][1]}，{lst_student[1][1]}，{lst_student[2][1]}，{lst_student[3][1]}，{lst_student[4][1]}，{lst_student[5][1]}")
for k in range(0, len(lst_student)):
    if int(lst_student[k][2]) > 19:
        print(lst_student[k])
