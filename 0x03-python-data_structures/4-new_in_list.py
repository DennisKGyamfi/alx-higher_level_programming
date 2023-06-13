#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_copied_list = my_list[:]
    if idx < 0 or idx > len(my_list) - 1:
        new_copied_list = my_list[:]
        return new_copied_list
    else:
        new_copied_list[idx] = element
        return new_copied_list
