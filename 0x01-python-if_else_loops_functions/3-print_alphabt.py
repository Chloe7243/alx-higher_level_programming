#!/usr/bin/python3
for n in range(26):
    if n == 16 or n == 4:
        continue
    print("{}".format(chr(n + 97)), end='')
