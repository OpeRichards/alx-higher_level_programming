#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

my_list2 = [1, 2, 3, 4]
max_value2 = max_integer(my_list2)
print("Max: {}".format(max_value2))

my_list3 = [9, -1, 2, 3, 4, -30, 2]
max_value3 = max_integer(my_list3)
print("Max: {}".format(max_value3))

my_list4 = [1, 1]
max_value4 = max_integer(my_list4)
print("Max: {}".format(max_value4))

my_list5 = [1]
max_value5 = max_integer(my_list5)
print("Max: {}".format(max_value5))

my_list6 = []
max_value6 = max_integer(my_list6)
print("Max: {}".format(max_value6))

my_list7 = [-1, -2, -3, -4]
max_value7 = max_integer(my_list7)
print("Max: {}".format(max_value7))