#!/usr/bin/python3
def pow(a, b):
    is_digit = str(a).isdigit() if a > 0 else str(-a).isdigit()
    is_digit = str(b).isdigit() if b > 0 else str(-b).isdigit()
    result = ''
    if is_digit:
        result = a ** b
    return result
