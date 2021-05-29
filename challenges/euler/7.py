"""
https://projecteuler.net/problem=7By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
https://projecteuler.net/problem=7
"""
import itertools

from computation.prime import primes


def f(n):
    return next(itertools.islice(primes(), n - 1, None))


print(f(10001))
