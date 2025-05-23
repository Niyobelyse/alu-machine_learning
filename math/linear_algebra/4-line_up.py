#!/usr/bin/env python3
"""
Module that contains a function to add two arrays element-wise
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.
    Args:
        arr1: A list of integers or floats.
        arr2: A list of integers or floats.
    Returns:
        A new list containing the element-wise sum of arr1 and arr2,
        or None if the shapes of arr1 and arr2 are not the same.
    """
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]