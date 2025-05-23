#!/usr/bin/env python3
"""
Function that calculates the shape of a matrix
"""


def matrix_shape(matrix):
    """
    Calculates the shape of a matrix
    
    payload:
        matrix: A list of lists representing a matrix
        
    response:
        A list of integers representing the shape of the matrix
    """
    if not matrix:
        return [0]
    
    shape = []
    current = matrix
    

    while isinstance(current, list) and current:
        shape.append(len(current))
        current = current[0]
    
    return shape