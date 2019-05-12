# 提示：文件不要起中文名字
# 定义一个全局变量
g_num = 10
print("函数外", id(g_num))


def modify():
    # 表示要修改全局变量
    global g_num
    # 定义了一个局部变量，内存地址要改变的时候用global
    g_num = 1
    print("函数内：", id(g_num))


modify()
print(g_num)

# 定义一个可变类型的全局变量
g_list = [1, 3]
print(id(g_list))


def modify():
    # 在原有列表增加一个数据，内存地址没有发生改变，就不需要global
    # global g_list内存地址不改变，加不加global是一样的效果
    # 加上global表示内存地址要发生变化
    global g_list
    g_list = [1, 1]
    # g_list.append(8)
    print(id(g_list))


modify()
print(g_list)
