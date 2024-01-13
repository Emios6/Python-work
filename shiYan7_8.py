# 第八题

lst_staff = ["李梅", "张富", "付妍", "赵诺", "刘江"]
dic_award = {'张富': 10000, '赵诺': 15000}
for i in lst_staff:
    if i in dic_award:
        print(i, end="发放年终奖：")
        print(dic_award[i], end="元")
        print("\n")
    else:
        print(f"{i}发放年终奖：5000元")
        print("\n")