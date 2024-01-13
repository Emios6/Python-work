

count = 0
for year in range (1000,2001):
    if ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0):
        print(year,end='\t')
        count=count+1
        if count % 5 == 0:
            print( )

















