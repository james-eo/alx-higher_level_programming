#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list[:x]:
            print(i, end="")
            count += 1
        print(my_list)
        return count
    except:
        print("Error while printing my_list")
        return 0