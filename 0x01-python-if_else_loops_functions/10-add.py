#!/usr/bin/python3
def add(a, b):
    is_digit = str(a).isdigit() if a > 0 else str(-a).isdigit()
    is_digit = str(b).isdigit() if b > 0 else str(-b).isdigit()
    sum = ''
    if is_digit:
        sum = a + b
    return sum
