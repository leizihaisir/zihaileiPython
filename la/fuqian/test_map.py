def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))


def m(x):
    if x % 2 == 0:
        return x / 2
    return x * x


array = map(m, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(array))

# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，
# Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
