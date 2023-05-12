#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
len_args = len(argv) - 1
if len_args != 3:
    print(f"Usage: {argv[0]} <a> <operator> <b>")
    exit(1)
a = int(argv[1])
b = int(argv[3])
operation = {'+':add, '-':sub, '*':mul, '/':div}
for op in operation:
    if argv[2] == op:
        print(f"{a} {op} {b} = {operation[op](a, b)}")
        exit (0)
print("Unknown operator. Available operators: +, -, * and /")
exit(1)
