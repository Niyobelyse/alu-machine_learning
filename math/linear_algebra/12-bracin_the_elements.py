#!/usr/bin/env python3
"""
Module that contains a function to perform element-wise operations on two matrices
"""
def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division on two matrices.
    Args:
        mat1: A numpy.ndarray representing the first matrix.
        mat2: A numpy.ndarray representing the second matrix.
    Returns:
        A tuple containing the element-wise sum, difference, product, and quotient of mat1 and mat2.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
