#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        w_average = 0
        for score, weight in my_list:
            weight_average += (score * w_average)
        return w_average
