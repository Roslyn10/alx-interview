#!/usr/bin/pythin3
"""A function that calculates the minimum operations"""


def minOperations(n):
    """
    Calaculates the minimun number of operations it
    takes to result in n H characters

    Args:
        n (int): The given number of operations needed

    Return:
        N number of operations
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
