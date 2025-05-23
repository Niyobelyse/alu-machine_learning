#!/usr/bin/env python3
"""
Module that contains a function to perform matrix multiplication
"""


from typing import List, Union
Matrix = List[List[Union[int, float]]]
def mat_mul(mat1: Matrix, mat2: Matrix) -> Union[Matrix, None]:
    """
    Multiplies two matrices.
    Args:
        mat1: A list of lists representing the first matrix.
        mat2: A list of lists representing the second matrix.
    Returns:
        A new list of lists representing the product of the two matrices,
        or None if the matrices cannot be multiplied.
    """
    if len(mat1[0]) != len(mat2):
        return None
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*mat2)] for row in mat1]