#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

tuple_aaa = (1, 2)
tuple_bbb = (1, 2)
tuple_2 = (1, 2, 3)
tuple_3 = (1, 2, 3)
tuple_4 = (1)
tuple_5 = ()
tuple_6 = (1)
tuple_7 = ()
print(add_tuple(tuple_aaa, tuple_aaa))
print(add_tuple(tuple_aaa, tuple_2))
print(add_tuple(tuple_2, tuple_aaa))
print(add_tuple(tuple_2, tuple_3))
print(add_tuple(tuple_5, tuple_aaa))
print(add_tuple(tuple_aaa, tuple_6))
print(add_tuple(tuple_5, tuple_7))