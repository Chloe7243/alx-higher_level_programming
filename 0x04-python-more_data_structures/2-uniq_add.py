#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    num, list_sum = my_list[0], 0
    for i, x in enumerate(my_list):
        if x > num or i == 0:
            list_sum += x
            num = x
    return list_sum
