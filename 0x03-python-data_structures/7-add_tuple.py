#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum1, sum2 = 0, 0
    for i in range(2):
        a = tuple_a[i] if len(tuple_a) > i else 0
        b = tuple_b[i] if len(tuple_b) > i else 0
        if i == 0:
            sum1 = a + b
        else:
            sum2 = a + b
    return sum1, sum2
