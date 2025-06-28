#!/usr/bin/env python3
"""Bayesian Probability Intersection"""
import numpy as np


def binomial_coefficient(n, k):
    """Custom binomial coefficient calculation"""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    k = min(k, n - k)
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i

    return result


def intersection(x, n, P, Pr):
    """Check for valid input parameters"""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not isinstance(Pr, np.ndarray) or Pr.ndim != 1 or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    if any(val < 0 or val > 1 for val in P):
        raise ValueError("All values in P must be in the range [0, 1]")
    if any(val < 0 or val > 1 for val in Pr):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    # Calculate the intersection in P and the corresponding prior beliefs in Pr
    intersection_values = np.array([binomial_coefficient(
        n, x) * p**x * (1 - p)**(n - x) * prior for p, prior in zip(P, Pr)])

    return intersection_values
