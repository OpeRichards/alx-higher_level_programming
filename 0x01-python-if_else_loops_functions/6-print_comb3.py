#!/usr/bin/python3
for num in range(0, 9):
    for numb in range(1, 10):
        if num > numb:
            continue
        elif num == 8 and numb == 9:
            print('{}{}'.format(num, numb))
        else:
            print('{}{}'.format(num, numb), end=', ')
