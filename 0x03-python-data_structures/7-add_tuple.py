#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2, b1, b2 = tuple_a[0], tuple_a[1], tuple_b[0], tuple_b[1]
    tuple_r = ((a1 + b1), (b2 + a2))
    return tuple_r
