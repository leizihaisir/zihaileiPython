import os

# 写文件
f = open('fileTest/test.txt', 'w')
f.write("hello world,my name is zihailei")
f.close()

# 读文件
try:
    nf = open('fileTest/test.txt', 'r')
    print(nf.read())
finally:
    if nf:
        nf.close()

# 打印操作系统类型
print(os.name)

# 获取详细的系统信息
print(os.uname())

print(os.path.split("fileTest/test.txt")[1])
print(os.path.splitext("fileTest/test.txt")[1])
print(os.path.splitdrive("fileTest/test.txt")[1])
