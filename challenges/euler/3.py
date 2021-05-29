# Problem 3: Find the largest prime factor of a given number N.
# https://projecteuler.net/problem=3
from computation.prime import primes_upto


# Straight Forward
def f(n):
    return max([p for p in primes_upto(n) if not n % p])
