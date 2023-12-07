#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    arr = list(a_dictionary.keys())
    arr.sort()
    for i in arr:
        print("{}: {}".format(i, a_dictionary.get(i)))
