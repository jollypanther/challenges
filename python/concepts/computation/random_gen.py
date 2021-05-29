import random


def f(n, len):
    for _ in range(n):
        yield [random.sample(range(10, 2, -1), len),
               [random.randrange(3, 10) for _ in range(len)]][random.randint(0, 1)]
