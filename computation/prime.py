import itertools
from math import sqrt


# Straight Forward
def is_prime1(n):
    if n < 2:  # to skip 0,1
        return False
    for i in range(2, n):
        if not n % i:
            return False
    return True


# Optimization
def is_prime(n):
    if n < 2:
        return False
    elif n <= 3:  # 2 or 3,  to save unnecessary computation below
        return True
    elif n % 2 == 0:  # all even numbers
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):  # sqrt(n) is the largest factor of n
        if not n % i:
            return False
    return True


def primes():
    return filter(is_prime, itertools.count(2))


# Straight Forward
def primes_range1(end, start=2):
    return (i for i in range(start, end + 1) if is_prime(i))


# Based on https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def primes_upto(end):
    sieves = [True] * end

    for i in range(2, end):
        # Prime Check for every number upto sqrt of count
        # because number following sqrt(count) would have been already marked by previous iteration
        if sieves[i]:
            yield i
            # Mark multiples of each number as False
            # numbers upto it square are already marked by previous iteration
            for m in range(2 * i, end, i):
                sieves[m] = False


def prime_range(start, end):
    for p in primes_upto(end):
        if p > start:
            yield p
