#!/bin/python3

import os
import re
import sys

# matrix would be an NxN list of lists:
# num of rows = num of row items
def matrix_print(mat: list):
    for r in mat:
        print('\t'.join(r))

def matrix_transpose(mat: list):
    items = range(0, len(mat[0]))
    return [[mat[i][k] for i in items] for k in items]

def matrix_read():
    # find num of row items from the first row
    mat = [input().split()]
    rows = range(1, len(mat[0]))
    mat.extend([input().split() for i in rows])
    return mat

# for example, try:
#   cat input.ex | python3 matrix_transpose.py
if __name__ == '__main__':
    mat = matrix_read()
    matrix_print(matrix_transpose(mat))
