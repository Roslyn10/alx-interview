#!/usr/bin/python3
"""
A function that determines the fewest number of coins,
needed to meet a given amount total
"""


def makeChange(coins, total):
    """Returns the total amount of coins needed to meet total
    Args:
        total: The total/ final amount of coins needed
        coins: the change given

    Returns:
        * If total is 0 or less, return 0
        * If total cannot be met by any number of coins, return -1
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for a in range(1, total + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[total] if dp[total] != total + 1 else -1
