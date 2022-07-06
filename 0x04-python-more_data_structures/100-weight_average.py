#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        w_average = 0
        for score, weight in my_list:
            weight_average += (score * w_average)
        return w_average
    return 0
