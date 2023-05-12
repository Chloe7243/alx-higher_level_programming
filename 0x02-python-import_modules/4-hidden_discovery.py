#!/usr/bin/python3
import hidden_4
names = dir(hidden_4)
for name in names:
    if '_' not in name[0]:
        print(name)
