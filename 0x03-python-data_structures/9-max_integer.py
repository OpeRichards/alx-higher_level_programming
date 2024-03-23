#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = my_list[0]
    for num in range(1, len(my_list)):
        if my_list[num] > max_num:
            max_num = my_list[num]
            return max_num
        else:
            len(my_list) == 0
            return 'None'
