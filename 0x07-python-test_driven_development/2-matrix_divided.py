#!/usr/bin/python3
"""
Module contains a matrix division function
"""


def matrix_divided(matrix, div):
    """Divides elements in matrix by div """
    outer_list = []
#   raising TypeError if div is not a number
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
#   raising TypeError if div is zero
    if div == 0:
        raise ZeroDivisionError('division by zero')
#   raising TypeError if matrix isnt a list
    if type(matrix) != list:
        raise TypeError('matrix must be a matrix (list of lists)\
 of integers/floats')

    for i in matrix:
        #   raises TypeError if element in matrix aren't a list
        if type(i) != list:
            raise TypeError('matrix must be a matrix\
 (list of list) of integers/floats')
        else:
            number_of_rows = len(matrix)
            #   delimiter serves as a bound for row comparison
            #   this prevents the comparison from going out of range
            delimiter = number_of_rows - 1
        for x in range(delimiter):
            #   raising TypeError if rows in the matrix aren't
            #   of the same size
            if len(matrix[x]) != len(matrix[x+1]):
                raise TypeError('Each row of the matrix must\
 have the same size')
        inner_list = []
        for j in range(len(i)):
            #   raising TypeError when elements in the matrix
            #   aren't integers
            if type(i[j]) not in [int, float]:
                raise TypeError('matrix must be a matrix\
 (list of lists) of integers/floats')
            quotient = round(i[j]/div, 2)
            inner_list.append(quotient)
        outer_list.append(inner_list)
    return (outer_list)
