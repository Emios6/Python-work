# 第21题

s = "Whether the weather be fine, or whether the weather be not. " \
    "Whether the weather be cold, or whether the weather be hot. " \
    "We will weather the weather whether we like it or not. "
s = s.lower()
s = s.replace(",", "")
s = s.replace(".", "")
list = s.split(' ')
for i in range(len(list)):
    if list[i] == '':
        list.pop(i)
list = set(list)
print(len(list))