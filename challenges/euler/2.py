# Problem 2: Find the sum of all the even-valued terms in the Fibonacci 
# sequence which do not exceed one million.

def fib():
    x, y = 0, 1

    while True:
        yield x
        x, y = y, x + y


def even(seq):
    for i in seq:
        if not i % 2:
            yield i


def under_1m(seq):
    for i in seq:
        if i > 1000000:
            break
        yield i


print(list(under_1m(even(fib()))))
