#!/usr/bin/env python3
"""Calculate sum of squares"""


def summation_i_squared(n):
    """Calculate sum of squares up to n"""
    if not isinstance(n, (int, float)) or n != int(n) or n < 1:
        return None
    return sum(map(lambda x: x*x, range(1, n+1)))
