#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [[i[j] ** 2 for j in range(len(i))] for i in matrix]
