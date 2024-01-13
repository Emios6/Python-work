# 第19题
n = int(input("请输入偏移数目："))
alb = {}
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# 创建初始字典
for i in list1:
    alb[i] = i

# 根据偏移数目定义新的对应关系
for i in list1:
    asc = ord(i)
    new_asc = asc + n
    if new_asc <= 122:
        alb[i] = chr(new_asc)
    elif new_asc > 122:
        alb[i] = chr(new_asc-122+96)

print(alb)
