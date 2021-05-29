import itertools

import random_gen

l1, l2 = random_gen.f(2, 5)
# generate cross pairs NOT product yet
pairs = itertools.product(l1, l2)


def f1():
    return (x * y for x, y in pairs)


def f2():
    return map(lambda x: x[0] * x[1], pairs)


print(list(f1()))
