#!/usr/bin/python3
'''
Given a number n, write a method that
calculates the fewest number of operations needed to
result in exactly n H characters in the file.

H => Copy All => Paste => HH => Paste =>HHH => Copy All
=> Paste => HHHHHH => Paste => HHHHHHHHH
'''


def minOperations(n):
    if n == 0:
        return 0
    if n == 1:
        return 2
    if n == 2:
        return 2

    if n % 2 == 0:
        return 2 + minOperations(n/2)
    if n % 3 == 0:
        return 3 + minOperations(n-3)
    else:
        return 1 + minOperations(n-1)
