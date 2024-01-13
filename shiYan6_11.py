list_info = [["李玉", "男", 25], ["金忠", "男", 23], ["刘妍", "女", 21], ["莫心", "女", 24], ["沈冲", "男", 28]]
while True:
    id = input("请输入要删除的员工姓名：")
    if id == '0':
        break
    else:
        for k in list_info:
            if k[0] == id:
                list_info.pop(list_info.index(k))
                continue
    print(list_info)

