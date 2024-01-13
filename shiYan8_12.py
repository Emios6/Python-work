import random
def redPo(t, n):
    for i in range(1, n):
        solo = random.uniform(0.01, t / (n - i + 1) * 2)  # 保证每个人获得红包的期望是total/num
        t = t - solo
        print("第{}位红包金额： {:.2f}元".format(i, solo))
    else:
        print("第{}位红包金额： {:.2f}元".format(n, t))


redPo(100, 15)
