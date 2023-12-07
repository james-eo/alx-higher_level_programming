#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    num = 0
    avg = 0

    for tup in my_list:
        num += tup[0] * tup[1]
        avg += tup[1]

    return (num / avg)
