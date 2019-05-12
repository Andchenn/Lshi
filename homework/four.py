# 使用for循环和while循环打印99乘法表


for i in range(1, 10):
    j = 1
    while j <= i:
        print("%d*%d=%d\t" % (j, i, i * j), end="")
        j += 1
    print("")
    i += 1
