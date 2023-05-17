#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    num = my_list[0];
    list_sum = num;
    for x in my_list:
        if x > num:
            list_sum += x
            num = x
    return list_sum
