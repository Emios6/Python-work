lst_student = ["001", "李梅", 19, "002", "刘祥", 20, "003", "张武", 18]
lst_student.append("004")
lst_student.append("刘宁")
lst_student.append(20)
lst_student.append("006")
lst_student.append("梁峰")
lst_student.append(19)
lst_student.insert(12, "005")
lst_student.insert(13, "林歌")
lst_student.insert(14, 20)
x1 = lst_student.index("003")
print(f"学号{lst_student[x1]},姓名{lst_student[x1+1]},年龄{lst_student[x1+2]}岁")
print(f"{lst_student[1]},{lst_student[4]},{lst_student[7]},{lst_student[10]},{lst_student[13]},{lst_student[16]}")
age = (int(lst_student[2]) + int(lst_student[5]) + int(lst_student[8]) + int(lst_student[11]) + int(lst_student[14]) + int(lst_student[17])) / 6
print("平均年龄是%0.0f岁" % age)


