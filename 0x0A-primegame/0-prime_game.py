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
MARIA = 0
BEN = 1


def is_prime(n):
    '''
    Check if number is a prime number.
    '''
    # Check if n is less than 2, which are not prime
    if n <= 1:
        return False
    # 2 and 3 are prime numbers
    if n <= 3:
        return True
    # Eliminate numbers divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check divisors from 5 to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_multiple(n, x):
    '''
    This function checks if n is a multiple of x.
    '''
    return n % x == 0


def isWinner(x, nums):
    '''
    This function determines the winner of the game.
    '''
    player = BEN

    primes = []
    for i in range(x):
        primes.append([j for j in range(1, nums[i]+1) if is_prime(j)])
    for prime in primes:
        if len(prime):
            num = prime.pop(0)

            for i in range(len(prime)):
                if is_multiple(num, prime[i]):
                    prime.pop(i)
                player = (player + 1) % 2
    if player == MARIA:
        return 'Maria'
    else:
        return 'Ben'


if __name__ == "__main__":
    winner = isWinner(5, [2, 5, 1, 4, 3])
    print(winner)
