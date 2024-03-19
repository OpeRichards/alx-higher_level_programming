#!/usr/bin/python3
# define function uppercase
def uppercase(str):
    for y in str:  # Each items in `str`
        # Check if each item is lower
        # if lower, turn it to uppercase
        if ord(y) >= ord('a') and ord(y) <= ord('z'):
            alph = chr(ord(y) - 32)
        else:
            # Leave as uppercase if already so
            alph = y
        # Print all items in `str`using uppercase
        print('{}'.format(alph), end='')
    # Add a new line
    print()
