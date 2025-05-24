#!/usr/bin/env python3
""" Module that contains a function to perform matrix multiplication
"""


def mat_mul(mat1, mat2):
    """
    Multiplies two matrices.
    Args:
        mat1: A list of lists representing the first matrix.
        mat2: A list of lists representing the second matrix.
    Returns:
        A new list of lists representing the product of mat1 and mat2,
        or None if the matrices cannot be multiplied.
    """
    if len(mat1[0]) != len(mat2):
        return None
    return [[sum(a * b for a, b in zip(row1, col2)) for col2 in zip(*mat2)]
            for row1 in mat1]
