#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    sum = 0
    for nums in argv[1:]:
        sum += int(nums)
print('{}'.format(sum))
