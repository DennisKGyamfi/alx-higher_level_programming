#!/usr/bin/python3
"""
Module contains the ``print_square`` function
"""


def text_indentation(text):
    """Prints a text with 2 new lines aftereach of
    these characters: . , ? and :"""
    counter = 0
    #   counter is is assigned '1' right after a punctuation
    if type(text) != str:
        raise TypeError('text must be a string')
    else:
        for i in text:
            if (i == '.') or (i == '?') or (i == ':'):
                print(f'{i}')
                counter = 1
                print()
            else:
                if i == ' ' and counter == 1:
                    continue
                else:
                    counter = 0
                if i:
                    print(i, end='')
