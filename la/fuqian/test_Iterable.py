from collections import Iterable, Iterator

# 测试那些数据类型可以被遍历
# 测试list
print(isinstance([], Iterable))

# 测试tuple
print(isinstance((1, 2, 3), Iterable))

# 测试字符串
print(isinstance("1234567", Iterable))

# 测试数字，无法遍历数字
print(isinstance(123, Iterable))

# 测试判断数组是否是Iterator类型，不是
print(isinstance([], Iterator))

# 测试通过iter函数将数组转成Iterator对象
print(isinstance(iter([]), Iterator))

num_list = [1, 2, 3, 4, 5]

# 测试for循环遍历
for x in num_list:
    print("for循环遍历：", x)

# 测试迭代器遍历
it = iter(num_list)
while True:
    try:
        print("迭代器遍历：", next(it))
    except StopIteration:
        break


# 凡是可作用于for循环的对象都是Iterable类型,
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列,
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
