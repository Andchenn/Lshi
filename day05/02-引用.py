# 引用：通俗理解就是程序中的数据在内存中的地址“简称内存地址”
# 底层：数据结构

# a存储的是一个内存地址，10的内存地址
a = 10
# b存储的是什么（也是内存地址，a的内存地址，10的内存地址）
b = a
# 打印内存地址
print("a的内存地址为", id(a))
print("a的内存地址为", id(b))

# 16进制的内存地址
print("a的内存地址为", hex(id(a)))
print("b的内存地址为", hex(id(b)))

# 相当于重新开辟一个内存空间，称内存地址
a=20
print("a的内存地址为",id(a))