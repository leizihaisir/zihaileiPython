from io import StringIO

f = StringIO()
f.write("hello world")
print(f.getvalue())

newFile = StringIO("hello!\nworld!")
print(newFile.readline())


# 很多时候，数据读写不一定是文件，也可以在内存中读写。
# StringIO顾名思义就是在内存中读写str。
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
