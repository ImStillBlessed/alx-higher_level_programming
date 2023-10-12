#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return None
    weight_sum = 0
    mul = 0
    for score, weight in my_list:
        mul = score * weight
        weight_sum += weight
    if weight_sum == 0:
        return 0
    return mul / weight_sum
