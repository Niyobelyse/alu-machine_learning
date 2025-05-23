#!/usr/bin/env python3
"""
Module that contains a function to perform element-wise operations on two matrices
"""


import numpy as np
def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division
    of two matrices.

    Args:
        mat1: A numpy.ndarray.
        mat2: A numpy.ndarray or a scalar.

    Returns:
        A tuple containing the element-wise sum, difference, product,
        and quotient of mat1 and mat2.
    """
    add = np.add(mat1, mat2)
    sub = np.subtract(mat1, mat2)
    mul = np.multiply(mat1, mat2)
    div = np.divide(mat1, mat2)
    
    return add, sub, mul, div