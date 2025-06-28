#!/usr/bin/env python3
"""Function that calculates the correlation of a matrix"""


import numpy as np


def correlation(C):
    """
    Calculates the correlation matrix.

    Parameters:
    - C: numpy.ndarray of shape (d, d) containing a covariance matrix

    Returns:
    - numpy.ndarray of shape (d, d) containing the correlation matrix
    """

    # Check if C is a numpy.ndarray
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    # Check if C is a square matrix
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    # Calculate the standard deviations(square roots of the diagonal elements)
    std_devs = np.sqrt(np.diag(C))

    # Compute the outer product of standard deviations
    outer_std_devs = np.outer(std_devs, std_devs)

    # Calculate the correlation matrix
    correlation_matrix = C / outer_std_devs

    return correlation_matrix


# If you'd like to test the function:
# if __name__ == '__main__':
#     C = np.array([[36, -30, 15], [-30, 100, -20], [15, -20, 25]])
#     Co = correlation(C)
#     print(C)
#     print(Co)
