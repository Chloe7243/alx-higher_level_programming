#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerator, denominator = 0, 0
    for x in my_list:
        num1, num2 = x
        numerator += num1 * num2
        denominator += num2
    return numerator / denominator
