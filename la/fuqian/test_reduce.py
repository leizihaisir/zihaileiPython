from functools import reduce


def add(x, y):
    return x + y


a = reduce(add, [1, 2, 3, 4, 5])
print(a)


# 字符串转数字
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def fn(x, y):
    return x * 10 + y


print(reduce(fn, map(char2num, '13579')))

print(list(map(char2num, '13579')))

print(reduce(fn, [1, 3, 5, 7, 9]))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
