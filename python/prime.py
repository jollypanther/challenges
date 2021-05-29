# Based on https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
import functools
from math import sqrt


# Straight Forward
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if not n % i:
            return False
    return True


def primes1(end, start=2):
    return (i for i in range(start, end + 1) if prime(i))


def primes(count):
    # Creating matrix of True for the given number
    sieves = [True] * count
    # Marking 0 ,1 as Non Prime
    sieves[0] = False
    sieves[1] = False

    # Prime Check for every number upto sqrt of count
    # because number following sqrt(count) would have been already marked by previous iteration
    for i in range(2, int(sqrt(count)) + 1):
        if sieves[i]: yield i
        # Mark multiples of each number as False
        # first or smallest multiple of any given number is n * 2
        for m in range(i * 2, count, i):
            sieves[m] = False

    functools.reduce()
