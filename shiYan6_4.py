lst_busstop = ["龙江新城市", "阳光广场", "汉江路", "嫩江路", "清凉山公园", "拉萨路", "五台山", "莫愁路"]

start = input("请输入起始站：")
end = input("请输入终点站：")

x1 = lst_busstop.index(start)
x2 = lst_busstop.index(end)
x3 = x2-x1
if x3 > 0:
    print(f"从{start}站到{end}站要乘坐{x3}站路")
else:
    print("您需要乘坐反方向线路")
