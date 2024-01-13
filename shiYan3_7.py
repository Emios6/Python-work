#汇率转换

#本金
a1 = eval(input("请输入要兑换的货币值："))
flag = input("请输入该货币的符号：")

if flag == "$" :
    a2=a1 * 6.868
    print("%s美元可以兑换人民币%.2f元"%(a1 , a2))
elif flag == "￥" :
    a2 = a1  / 6.868
    print("%s人民币可以兑换美元%.2f元" % (a1 , a2))
