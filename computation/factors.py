# straightforward
def factor1(n):
    if n == 1:
        yield 1
    for i in range(1, n):
        if not n % i:
            yield i


# Efficient
def factor(n):
    if n == 1:
        yield 1
    i = 1
    m = n

    while i < m:
        if not n % i:
            yield i
            q = n // i
            if i == q:
                break
            yield q
            m = q
        i += 1
        m -= 1
