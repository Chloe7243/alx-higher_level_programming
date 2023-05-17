#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = my_list.copy()
    for i, x in enumerate(n_list):
        if x == search:
            n_list.pop(i)
            n_list.insert(i, replace)
    return n_list
