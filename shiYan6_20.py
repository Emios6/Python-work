import random
lst_1 = ["黑桃", "红桃", "梅花", "方块"]
lst_2 = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
lst_3 = []
for x1 in lst_2:
    for x2 in lst_1:
        lst_3.append(x1+" "+ x2)

print(lst_3)

random.shuffle(lst_3)

k1 = int(input("请输入0~51的序号："))

k2 = random.randint(0,51)
if k1 < k2:
    print("很遗憾，您输了！")
if k1>k2:
    print("恭喜，您赢了！")
if k1==k2:
    print("咱们平手了！")