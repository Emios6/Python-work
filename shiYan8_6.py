def isLeap(x):
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        return 1
    else:
        return 0


countYear = 0
for year in range(1900, 2021):
    if isLeap(year) == 1:
        countYear += 1
        print(year, end=' ')
        if countYear % 5 == 0:
            print("\n")