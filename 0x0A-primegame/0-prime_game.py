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

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = generate_primes(n)
        turn = 0

        while primes:
            current_prime = primes.pop(0)
            primes = [p for p in primes if p % current_prime != 0]
            turn = 1 - turn

        if turn == 1:
            ben_wins += 1
        else:
            maria_wins += 1

        if maria_wins > ben_wins:
            return "Maria"
        elif ben_wins > maria_wins:
            return "Ben"
        else:
            return None
