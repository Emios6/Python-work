# 根据字符串输入实现各种需求

s = input("请输入字符串：")

count = s.count('t')
l = s.index('com')
s1 = s[7:13]
s2 = s[-12:-8]
s3 = s.upper()
s4 = len(s)
s5 = s + "index"
print(f"字符串中字母t出现的次数：{count}")
print(f"字符串中‘com’子字符出现的位置：{l}")
print(f"正向切片提取”sports“: {s1}")
print(f"反向切片提取”sina“: {s2}")
print(f"将字符串中的字母全都变为大写之后的字符串是：{s3}")
print(f"字符串的总字符个数是：{s4}")
print(f"在后面拼接index后的字符串：{s5}")