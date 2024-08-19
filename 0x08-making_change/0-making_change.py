#!/usr/bin/python3
'''
Module for making_change
'''


def makeChange(coins, total):
    '''
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total
    Args:
        coins: list of coins
        total: amount
    Returns:
        fewest number of coins needed
    '''
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += total // coin
        total = total % coin
    if total > 0:
        return -1
    return count
