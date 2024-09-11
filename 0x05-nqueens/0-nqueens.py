#!/usr/bin/python3
"""A module that solves the NQueens leetcode problem"""


import sys


class Solution:
    """A class that contains the contents of the solution to the leetcode"""
    def NQueens(self, n):
        """Sets up the board for the code"""
        col = set()
        posDiag = set()
        negDiag = set()

        result = []
        positions = []

        def backtrack(r):
            """A function that ensures that the positions of the queens aren't
            able to attack another queen on the board"""
            if r == n:
                result.append(positions.copy())
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                positions.append([r, c])

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                positions.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 0-nqueens.py <n>")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: n must be an integer.")
        sys.exit(1)

    sol = Solution()
    output = sol.NQueens(n)
    print(output)
