#!/usr/bin/python3
def no_c(my_string):
    for xs in my_string:
        if xs != 'c':
            if xs != 'C':
                print('{}'.format(xs), end='')
    return ''
