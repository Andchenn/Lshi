# 定义一个带有参数的装饰器函数
# get函数的目的就是返回一个装饰器函数


def get_decorator(char):
    def decorator(func):
        def inner():
            print(char)
            func()

        return inner

    return decorator


@get_decorator("AAA")
def show():
    print("222")


show()
