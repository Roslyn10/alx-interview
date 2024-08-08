#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascals triangle of n
    """

    triangle = []

    if n <= 0:
        return []

    for n in range(n):
        row = []
        for k in range(n + 1):
            coeff = factorial(n) // (factorial(k) * factorial(n - k))
            row.append(coeff)
        triangle.append(row)

        return triangle

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
