#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    num, list_sum = my_list[0], 0
    for x in my_list:
        if x > num:
            list_sum += x
            num = x
    return list_sum
