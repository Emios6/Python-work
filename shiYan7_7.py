# 第七题

dic_user = {'John': 123, 'Marry': 111, 'Tommy': 123456}
userName = input("请输入用户名：")
userSecret = int(input("请输入密码："))
if userName not in dic_user:
    print("用户名错误！")
else:
    if dic_user[userName] != userSecret:
        print("密码错误！")
    else:
        print("登录成功！")
