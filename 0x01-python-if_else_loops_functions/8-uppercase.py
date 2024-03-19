#!/usr/bin/python3
def uppercase(str):
    for y in str:
        if ord(y) >= ord('a') and ord(y) <= ord('z'):
            alph = chr(ord(y) - 32)
        else:
            alph = y

        print('{}'.format(alph), end='')
    print()
