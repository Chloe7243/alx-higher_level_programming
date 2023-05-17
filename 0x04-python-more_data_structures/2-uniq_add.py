#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    num, list_sum = 0, 0
    for x in my_list:
        if x > num:
            list_sum += x
            num = x
    return list_sum

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
