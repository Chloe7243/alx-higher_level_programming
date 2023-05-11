#!/usr/bin/python3
def print_last_digit(number):
    if str(number).isdigit():
        last_digit = str(number)[-1]
        print("{}".format(last_digit), end='')
        return last_digit
