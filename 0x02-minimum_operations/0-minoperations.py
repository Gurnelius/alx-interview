#!/usr/bin/python3
'''
Given a number n, write a method that
calculates the fewest number of operations needed to
result in exactly n H characters in the file.

H => Copy All => Paste => HH => Paste =>HHH => Copy All
=> Paste => HHHHHH => Paste => HHHHHHHHH
'''


def minOperations(n):
    """
    Calculates the minimum number of operations needed to
    obtain a string of 'H' characters of length `n`.

    Parameters:
        n (int): The desired length of the string.

    Returns:
        int: The minimum number of operations needed.

    """

    if n < 2:
        return 0

    if n % 2 == 0:
        return 2 + minOperations(n/2)
    if n % 3 == 0:
        return 3 + minOperations(n/3)
    else:
        return 1 + minOperations(n-1)
