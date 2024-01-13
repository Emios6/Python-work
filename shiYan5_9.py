a = input("请输入初始项：")
n = int(input("请输入项数："))
s = 0
num = int(a)

for i in range(n):
    s += num
    num = num * 10 + int(a)

print(f"s = {s}")


