def is_odd(x):
    return x % 2 == 0


a = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(a))


def _odd_iter():
    n = 1
    while n <= 100:
        n = n + 2
        yield n


# 生成一个判断函数
def _not_divisible(n):
    return lambda x: x % n > 0


print("开始打印素数")


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的下一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印100以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break
