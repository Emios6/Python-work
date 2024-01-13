list_floor = [1, 4, 2, 5, 7, 3]
for k in range(1, len(list_floor)):
    x1 = list_floor[k]
    x2 = list_floor[k-1]
    if x1 > x2:
        x3 = x1 - x2
        print("上"*x3, end="")
    else:
        x4 = x2 - x1
        print("下"*x4,end="")
print(" ")
lst_l = ["上", "上", "下", "下", "下", "上", "上", "下", "上", "上", "上", "上"]
floor1 = 2
print(floor1, end=" ")
for m in range(0, 12):
    if lst_l[m] == "上":
        floor1 = floor1+1
        print(floor1, end=" ")
    if lst_l[m] == "下":
        floor1 = floor1-1
        print(floor1, end=" ")