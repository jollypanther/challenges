# A product of iterable
import math
import operator
from functools import reduce

import numpy


def f1(l):
    res = 1
    for i in l:
        res *= i
    return res


def f2(l):
    return math.prod(l) or numpy.prod(l)


def f3(l):
    return reduce(operator.mul, l) or reduce(lambda x, y: x * y, l)


l = range(1, 5)

print(f1(l), f2(l), f3(l))
