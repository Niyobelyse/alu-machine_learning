#!/usr/bin/env python3
"""
Module that contains a function to concatenate two matrices along a specific axis
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.
    Args:
        mat1: A list of lists representing a matrix.
        mat2: A list of lists representing a matrix.
        axis: The axis along which to concatenate the matrices (0 for rows, 1 for columns).
    Returns:
        A new list of lists representing the concatenated matrix,
        or None if the matrices cannot be concatenated.
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None