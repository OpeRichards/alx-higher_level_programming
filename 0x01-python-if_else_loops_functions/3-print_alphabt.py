#!/usr/bin/python3
for num in range(97, 123):
    if chr(num) != 'e' and chr(num) != 'q':
        print('{}'.format(chr(num)), end='')
