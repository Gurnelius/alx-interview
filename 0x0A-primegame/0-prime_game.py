#!/usr/bin/python3
'''
Maria and Ben are playing a game. Given a set of consecutive integers starting
from 1 up to and including n, they take turns choosing a prime number from the
set and removing that number and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.
'''


def sieve(n):
    """
    Return a list of prime numbers up to n using the
    Sieve of Eratosthenes.
    """
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def isWinner(x, nums):
    """Determine who won the most rounds."""
    if x <= 0 or not nums:
        return None

    # Maximum number in nums
    max_n = max(nums)

    # Get list of primes up to max_n using sieve
    primes = sieve(max_n)

    # Track the number of wins
    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        prime_count = 0
        for p in primes:
            if p > n:
                break
            # How many primes <= n
            prime_count += 1

        # If the count of primes up to n is odd, Maria wins, else Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
