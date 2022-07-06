#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        w_average = 0
        total_weight = 0
        for score, weight in my_list:
            w_average += (score * weight)
            total_weight += weight
        return w_average / total_weight
