#!/usr/bin/env python3
"""Function that calculates the mean and covariance of a dataset"""


import numpy as np


def mean_cov(X):
    """
    Calculates the mean and covariance of a dataset

    Parameters:
    - X: numpy.ndarray of shape (n, d) containing the dataset

    Returns:
    - mean: numpy.ndarray of shape (1, d) containing the mean of the dataset
    - cov: numpy.ndarray of shape (d, d) containing the covariance
    """

    # Check if X is a 2D numpy.ndarray
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    n, d = X.shape

    # Check if n is less than 2
    if n < 2:
        raise ValueError("X must contain multiple data points")

    # Calculate the mean of the dataset
    mean = np.mean(X, axis=0).reshape(1, d)

    # Calculate the covariance matrix
    deviation = X - mean
    cov = np.dot(deviation.T, deviation) / (n - 1)

    return mean, cov


# # If you'd like to test the function:
# if __name__ == '__main__':
#     np.random.seed(0)
#     X = np.random.multivariate_normal(
#         [12, 30, 10], [[36, -30, 15], [-30, 100, -20], [15, -20, 25]], 10000)
#     mean, cov = mean_cov(X)
#     print(mean)
#     print(cov)
