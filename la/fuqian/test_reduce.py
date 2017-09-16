from functools import reduce


def add(x, y):
    return x + y


a = reduce(add, [1, 2, 3, 4, 5])
print(a)


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def fn(x, y):
    return x * 10 + y



print(reduce(fn, map(char2num, '13579')))

print(list(map(char2num, '13579')))






