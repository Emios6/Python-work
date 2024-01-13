# 第22题
set_highjump = {"李朋", "王宇", "张锁", "刘松山", "白旭", "李晓亮"}
set_longjump = {"王宇", "唐英", "刘松山", "白旭", "刘小雨", "宁成"}

print(f"参加比赛的所有学生：{set_longjump.symmetric_difference(set_highjump)}{set_longjump & set_highjump}")
print(f"两项比赛都参加的学生：{set_longjump & set_highjump}")
print(f"仅参加跳高的学生：{set_highjump - set_longjump}")
print(f"仅参加跳远的学生：{set_longjump - set_highjump}")
print(f"仅参一项比赛的学生：{set_longjump - set_highjump }{set_highjump - set_longjump}")

