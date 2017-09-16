def higher_order_test(x, y, f):
    return f(x) + f(y)


a = higher_order_test(3, -19, abs)
print(a)
