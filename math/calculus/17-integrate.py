#!/usr/bin/env python3
"""Derivative of a polynomial"""


def poly_integral(poly, C=0):
    """Calculates the integral of a polynomial"""
    integral = []
    # check for the validity of the inputs
    if not isinstance(poly, list) or len(poly) == 0 or not isinstance(C, int):
        return None
    # calculate the cofficients
    for i in range(len(poly)-1, 0, -1):
        integral.append(poly[i]/(i+1))

    integral.append(poly[0])
    integral.append(C)
    # fit the output like on the intranet
    if len(poly) == 1 and poly[0] == 0:
        integral = [C]
    for i in range(len(integral)):
        if integral[i] % 1 == 0:
            integral[i] = int(integral[i])

    return integral[::-1]
