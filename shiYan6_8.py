import random

list = ['A', 'B', 'C', 'D', 'E']


while True:
    if((list[1] == 'D')+(list[2] == 'B') == 1 and (list[1] == 'C') + (list[3] == 'E') == 1 and (list[0] == 'E') + (list[4] == 'A') == 1 and (list[2] == 'C') + (list[3] == 'A') == 1 and (list[1] == 'B') + (list[4] == 'D') == 1):
         print(list)
         break
    else:
        random.shuffle(list)
