#!/usr/bin/python3
def multiple_returns(sentence):
    my_tup = ()
    if len(sentence) == 0:
        my_tup = 0, "None"
    else:
        my_tup = len(sentence), sentence[0]
    return my_tup
