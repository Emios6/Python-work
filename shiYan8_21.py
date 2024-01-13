def encrypt(s):
    list1 = []
    for i in range(len(s)):
        a1 = int(s[i]) + 5
        a2 = a1 % 10
        list1.append(str(a2))
    list1 = list1[::-1]
    fin = ""
    for i in list1:
        fin += i
    return fin


print(encrypt("2345"))
