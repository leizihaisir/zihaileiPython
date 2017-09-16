def lazy_sun(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax

    return sum


f = lazy_sun(1, 2, 3, 4, 5, 6, 7, 8, 9)
# 执行函数才能求和
print("求和值：", f())
f1 = lazy_sun(1, 2, 3, 4, 5, 6, 7, 8, 9)

# 返回值为函数的同阶函数同参函数的返回值不相等
print("返回值为函数的同阶函数同参函数是否相等", f == f1)


# 总结：一个函数的返回值不一定全是确定结果，也可能是函数，返回函数是要防止闭包问题
