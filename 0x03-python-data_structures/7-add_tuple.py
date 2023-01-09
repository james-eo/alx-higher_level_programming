#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = list(tuple_a)
    tuple_2 = list(tuple_b)

    tuple_1.extend((0, 0))
    tuple_2.extend((0, 0))

    sum_1 = tuple_1[0] + tuple_2[0]
    sum_2 = tuple_1[1] + tuple_2[1]
    return (sum_1, sum_2)
