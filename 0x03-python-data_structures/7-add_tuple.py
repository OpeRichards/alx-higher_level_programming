#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_2a = tuple_a + (0, 0)
    tuple_2b = tuple_b + (0, 0)
    sum_tuple = tuple([tuple_2a[xrs] + tuple_2b[xrs] for xrs in range(len(tuple_a))])
    return sum_tuple
