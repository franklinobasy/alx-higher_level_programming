#!/usr/bin/python3
"""
Module composed by a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices
    Args:
        m_a: matrix a
        m_b: matrix b
    Returns:
        result of the multiplication
    Raises:
        TypeError: if m_a or m_b aren't a list
        TypeError: if m_a or m_b aren't a list of a lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b don't have integers or floats
        TypeError: if the rows of m_a or m_b don't have the same size
        ValueError: if m_a and m_b can't be multiplied
    """
    nrow, ncol = validateMat(m_a, m_b)
    m_b_T = transpose(m_b)

    linear_v = []
    for row in m_a:
        for col in m_b_T:
            linear_v.append(dot_product(row, col))

    return linear_to_shape(linear_v, ncol, nrow)


def dot_product(v1, v2):
    """Function to perform dot product
    Args:
        v1: vector1
        v2: vector2

    Returns:
        scalar result
    """
    sum = 0
    for i, j in zip(v1, v2):
        sum += (i * j)

    return sum


def validateMat(mat_A, mat_B):
    """Function to validate matrices
    Args:
        mat_A: matrix A
        mat_B: matrix B

    Returns:
        number of rows and number of cols
    """
    if not isinstance(mat_A, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(mat_A[0], list):
        raise TypeError("m_a must be a list of lists")
    else:
        for row in mat_A[1:]:
            if not isinstance(row, list):
                raise TypeError("m_a must be a list of lists")

    if not isinstance(mat_B, list):
        raise TypeError("m_b must be a list")
    elif not isinstance(mat_B[0], list):
        raise TypeError("m_b must be a list of lists")
    else:
        for row in mat_B[1:]:
            if not isinstance(row, list):
                raise TypeError("m_b must be a list of lists")

    try:
        if not mat_A or not mat_A[0]:
            raise ValueError("m_a can't be empty")
    except IndexError:
        raise ValueError("m_a can't be empty")

    try:
        if not mat_B or not mat_B[0]:
            raise ValueError("m_b can't be empty")
    except IndexError:
        raise ValueError("m_b can't be empty")

    for row in mat_A:
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in mat_B:
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    for i in range(1, len(mat_A)):
        if len(mat_A[i]) != len(mat_A[i-1]):
            raise TypeError("each row of m_a must be of the same size")

    for i in range(1, len(mat_B)):
        if len(mat_B[i]) != len(mat_B[i-1]):
            raise TypeError("each row of m_b must be of the same size")

    ncol = len(mat_A[0])

    nrow = 0
    for row in mat_B:
        nrow += 1

    if ncol == nrow:
        return (nrow, ncol)

    raise ValueError("m_a and m_b can't be multiplied")


def transpose(mat):
    """Function to transpose a matrix
    Args:
        mat: Matrix to transpose

    Returns:
        tranposed matrix
    """
    ncol = len(mat[0])
    nrow = 1
    for row in mat[1:]:
        nrow += 1
        if len(row) != ncol:
            return ValueError("m_a and m_b can't be multiplied")

    matT = [[0 for j in range(nrow)] for i in range(ncol)]

    for j in range(ncol):
        for i in range(nrow):
            matT[j][i] = mat[i][j]

    return matT


def linear_to_shape(linear_v, nrow, ncol):
    """converts a vector to nrow x ncol matrix
    Args:
        linear_v: 1D vector
        nrow: number of rows
        ncol: number of columns

    Returns:
        nrow x ncol matrix
    """
    mat = []
    vector = linear_v.copy()
    for i in range(nrow):
        temp = []
        try:
            for j in range(ncol):
                temp.append(vector.pop(0))
            mat.append(temp)
        except IndexError:
            break

    return mat
