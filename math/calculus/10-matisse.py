#!/usr/bin/env python3
"""Calculate the derivate of a polynomial vector"""


def poly_derivative(poly):
    """Calculate the derivate of vector poly"""
    try:
        iter(poly)
    except TypeError:
        return None
    if poly == [] or any(not isinstance(coef, (int, float)) for coef in poly):
        return None
    if len(poly) == 1:
        return [0]
    return [i*coef for i, coef in enumerate(poly)][1:]
