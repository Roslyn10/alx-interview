#!/usr/bin/python3
"""
Module: Game of choosing Prime numbers
"""


def generate_primes(n):
    """
    Helper function that generates numbers and
    checks if they are prime numbers

    Args:
        is_prime: empty list
        fil_prime: a list of numbers that are set to true

    Return:
        returns the prime numbers
    """
    is_prime = []
    fil_prime = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (fil_prime[prime]):
            is_prime.append(prime)
            for i in range(prime, n + 1, prime):
                fil_prime[i] = False
    return is_prime


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): number  of rounds per game
        nums (int): the nth number in the game
    Return:
        Name of the Winner either
        Ben or Maria
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for p in range(x):
        is_prime = generate_primes(nums[p])
        if len(is_prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
