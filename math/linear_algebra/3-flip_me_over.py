# #!/usr/bin/env python3
def matrix_transpose(matrix):
    """
    Transpose a 2D matrix

    Args:
        matrix: A list of lists representing a matrix

    Returns:
        A new list of lists representing the transposed matrix
    """
    if not matrix or not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        return []

    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]