#!/usr/bin/python3
"""
Module contains ``matrix_mul``:
a matrix multiplication function
"""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""
    #   adding exceptions
    if type(m_a) not in [list]:
        raise TypeError('m_a must be a list')
    if type(m_b) not in [list]:
        raise TypeError('m_b must be a list')
    #   exception for m_a not being list of list
    for i in m_a:
        if type(i) is not list:
            raise TypeError('m_a must be a list of lists')
    #   exception for elements in m_a not being ints and floats
        for x in i:
            if type(x) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    #   exception for m_b not being list of list
    for i in m_b:
        if type(i) is not list:
            raise TypeError('m_b must be a list of lists')
    #   exception for elements in m_b not being ints and floats
        for x in i:
            if type(x) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    #   exceptions for either m_a or
    #   m_b being empty lists or empty list of lists
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    #   exception for the rows in m_a not being the same size
    number_of_rows = len(m_a)
    #   delimiter serves as a bound for row comparison
    #   this prevents the comparison from going out of range
    delimiter = number_of_rows - 1
    for x in range(delimiter):
        #   raising TypeError if rows in the matrix aren't
        #   of the same size
        if len(m_a[x]) != len(m_a[x+1]):
            raise TypeError('each row of m_a\
 must be of the same size')

    #   exception for the rows in m_b not being the same size
    number_of_rows = len(m_b)
    #   delimiter serves as a bound for row comparison
    #   this prevents the comparison from going out of range
    delimiter = number_of_rows - 1
    for x in range(delimiter):
        #   raising TypeError if rows in the matrix aren't
        #   of the same size
        if len(m_b[x]) != len(m_b[x+1]):
            raise TypeError('each row of m_b\
 must be of the same size')
    # raising an exception if m_a and m_b can't be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    inverted_b = []
    for Row in range(len(m_b[0])):
        new_row = []
        for Column in range(len(m_b)):
            new_row.append(m_b[Column][Row])
        inverted_b.append(new_row)
    new_matrix = []
    for row in m_a:
        new_row = []
        for column in inverted_b:
            product = 0
            for i in range(len(inverted_b[0])):
                product += row[i] * column[i]
            new_row.append(product)
        new_matrix.append(new_row)
    return new_matrix
