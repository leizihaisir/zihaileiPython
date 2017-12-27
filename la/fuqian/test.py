from collections import Iterable


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-910))

print(isinstance("String", Iterable))

listStr = list(range(1, 11))
listStr.append(11)
print("listStr的length：", len(listStr))
print(listStr)
print("切前五个", listStr[0:5], "数组")
var_list = ['tom', 'david', 'john']
a = '###'
print(a.join(var_list[0:2]))
print([x * x for x in range(1, 11)])
