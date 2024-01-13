def f1(arr, target):
    deep = 0
    top = len(arr) - 1
    while deep <= top:
        mid = (deep + top) // 2
        mid_value = arr[mid]
        if mid_value == target:
            return mid
        elif mid_value < target:
            deep = mid + 1
        else:
            top = mid - 1
    return -1


list1 = input("请输入整数列表（以空格分隔）: ").split()
list2 = [int(num) for num in list1]

target_num = int(input("请输入要查找的目标数字: "))

result = f1(list2, target_num)

# 输出结果
if result != -1:
    print(f"目标数字在列表中的索引为 {result}.")
else:
    print(result)
