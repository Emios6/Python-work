
a1 = 1
a2 = 1
count = 0

for n in range (1 , 21):
    print(a1,end='\t')
    t = a1
    a1 = a2
    a2 = t + a2
    count = count + 1

    if count % 5 == 0:
        print()

