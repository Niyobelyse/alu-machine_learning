#!/usr/bin/env python3
"""
Module that contains a function to add two matrices element-wise
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two matrices element-wise.
    Args:
        mat1: A list of lists representing a matrix.
        mat2: A list of lists representing a matrix.
    Returns:
        A new list of lists representing the element-wise sum of mat1 and mat2,
        or None if the shapes of mat1 and mat2 are not the same.
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    return [[a + b for a, b in zip(row1, row2)]
            for row1, row2 in zip(mat1, mat2)]