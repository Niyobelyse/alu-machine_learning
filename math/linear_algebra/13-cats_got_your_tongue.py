#!/usr/bin/env python3
"""
Module that contains a function to concatenate two matrices
"""
def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.
    Args:
        mat1: A numpy.ndarray representing the first matrix.
        mat2: A numpy.ndarray representing the second matrix.
        axis: The axis along which to concatenate the matrices
              (0 for rows, 1 for columns).
    Returns:
        A new numpy.ndarray representing the concatenated matrix,
        or None if the matrices cannot be concatenated.
    """
    return np_cat.concatenate((mat1, mat2), axis=axis)

