import random

list_who = ['小马', '小羊', '小鹿']
list_where = ['草地上', '电影院', '家里']
list_what = ['看电影', '听故事', '吃晚饭']

x1 = random.randint(0, 2)
x2 = random.randint(0, 2)
x3 = random.randint(0, 2)

print(f"{list_who[x1]}在{list_where[x2]}{list_what[x3]}")



