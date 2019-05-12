# 定义不定长位置参数
def show_msg(*args):
    print(args)


# 定义不定长位置参数
def show(*args):
    # print(args, type(args))

    print(args)
    # 解决办法：对元组进行拆包
    show_msg(*args)

    # show_msg(args)


show(1, 2)
