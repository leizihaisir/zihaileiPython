def fact(n):
    if 1 == n:
        return n
    else:
        return n * fact(n - 1)


print(fact(5))
