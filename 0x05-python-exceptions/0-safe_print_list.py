#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for j in range(x):
            print("{}".format(my_list[j]), end='')
        print()
        return x
    except IndexError:
        print()
        return j
