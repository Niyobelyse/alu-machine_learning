#!/usr/bin/env python3
"""
Function that calculates the shape of a numpy.ndarray
"""
import numpy as np
def np_shape(matrix):
    """
    Calculates the shape of a numpy.ndarray

    Args:
        matrix: A numpy.ndarray

    Returns:
        A tuple of integers representing the shape of the matrix
    """
    return np.shape(matrix)