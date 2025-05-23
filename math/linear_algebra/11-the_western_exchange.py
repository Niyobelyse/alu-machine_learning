#!/usr/bin/env python3
"""
Module that contains a function to transpose a matrix
"""

import numpy as np
def np_transpose(matrix):
    """
    Transposes a matrix.
    Args:
        matrix: A numpy.ndarray representing a matrix.
    Returns:
        A new numpy.ndarray representing the transposed matrix.
    """
    return matrix.T