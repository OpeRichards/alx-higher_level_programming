#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_2a = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    tuple_2b = tuple_b[:2] + (0,) * (2 - len(tuple_b))
    sum_tuple = tuple([tuple_2a[xrs] + tuple_2b[xrs] for xrs in range(2)])
    return sum_tuple
