lst_fib = [1, 1]

for x in range(2, 30):
    y = lst_fib[x-2]+lst_fib[x-1]
    lst_fib.append(y)

print(lst_fib)

