#!/usr/bin/python3
def print_last_digit(number):
    last_digit = str(number)[-1] if 9 >= int(str(number)[-1]) >= 0 else ''
    print("{}".format(last_digit), end='')
    return last_digit
