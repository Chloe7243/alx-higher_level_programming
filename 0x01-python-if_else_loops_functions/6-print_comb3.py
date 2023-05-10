#!/usr/bin/python3
for n in range(1,100):
    if (n < 10 or str(n)[0] < str(n)[1]):
        print("{:02d}".format(n), end='')
        print(', ' if n != 89 else '\n', end='')
