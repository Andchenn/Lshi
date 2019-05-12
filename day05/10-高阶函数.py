# 高阶函数：当一个函数的参数，可以接收另外一个函数
# 函数作为参数
# 或者还可以返回一个函数，那么这个函数就叫高阶函数
# 只有参数是函数的高阶函数


def sum_num(num1, num2):
    result = num1 + num2
    return result


# 高阶函数，接收参数为函数
def calc_num(new_func):
    # new_func就是外部传来的函数
    result = new_func(2, 2)
    print(result)


# 调用clac_num函数(参数为sum_num的函数)
calc_num(sum_num)


# print(result)


# 高阶函数：还可以返回函数，既有参数是函数，又有返回值是函数


def text(new_func):
    # 调用传入的外部函数
    new_func()

    # 内部函数
    def inner():
        print("我是内部函数")

    return inner


# 需要传入的参数函数
def show_msg():
    print("今天天气很好")


# 调用高阶函数
# new_func就是text函数里面的inner
new_func = text(show_msg)
new_func()
# 没有返回值
# print(result)
