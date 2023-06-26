#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    val = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            val += 1
        except (ValueError, TypeError):
            pass
    print()
    return val
