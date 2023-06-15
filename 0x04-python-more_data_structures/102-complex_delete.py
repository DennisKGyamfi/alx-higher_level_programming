#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    dict_copy = my_dict.copy()

    for k, v in dict_copy.items():
        if value == v:
            del a_dictionary[k]
    return (a_dictionary)
