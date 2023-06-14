#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multip = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multip.append(True)
        else:
            multip.append(False)

    return (multip)
