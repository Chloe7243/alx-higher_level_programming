#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    if len(str) <= n or 0 > n > -(len(str)):
        return str
    for c in str:
        if c == str[n]:
            continue
        new_str += c
    return new_str
