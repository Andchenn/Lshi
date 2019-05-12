# 全局变量：在函数外定义的变量叫全局变量
# 特点：全局变量可以在不同的函数里面使用

score = 100


def show():
    # 定义了一个局部变量，只不过这个局部变量和全局变量的名字一样
    # 表示要对全局变量score修改数据
    global score
    score = 99
    # 修改全局变量
    print(score)


show()
print(score)
