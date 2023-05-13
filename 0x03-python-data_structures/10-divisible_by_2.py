#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    n_list = []
    for n in my_list:
        if n % 2 == 0:
            n_list.append(True)
        else:
            n_list.append(False)
    return n_list
