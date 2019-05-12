# 装饰器:本质上就是一个函数，可以给原函数增加新的功能(不改变函数的情况下)


def decorator(new_func):
    def inner():
        print("+++")
        new_func()

    # 注意返回函数要是函数的名字，如果加括号等于调用函数
    return inner


# 语法糖 相当于inner=decorator(show)
@decorator
def show():
    print("BBB")


show()
