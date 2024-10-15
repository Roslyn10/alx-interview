#!/usr/bin/python3
"""Prime game"""


def isWinner(x, nums):
    """"
    Main function that simulates the game play
    """
    def generate_primes(n):
        """
        Helper function that generates numbers and
        checks if they are prime numbers
        """
        is_prime = [True for i in range(n + 1)]
        is_prime[0] = is_prime[1] = False

        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1

        return [p for p in range(2, n + 1) if is_prime[p]]

    Maria = 0
    Ben = 0

    for i in range(x):
        prime = generate_primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
