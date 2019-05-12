# 通用的装饰器，可以修饰任意函数
# 定义一个带有参数的函数(2个,3个)


def decorator(func):
    # 嵌套函数
    def inner(*args, **kwargs):
        print("计算结果如下：")
        result = func(*args, **kwargs)
        return result

    return inner


@decorator
def sum(num1, num2):
    result = num1 + num2
    # print(result)
    return result


result = sum(2, 3)
print(result)

@decorator
def sum(num1, num2,num3):
    result = num1 + num2+num3
    # print(result)
    return result


result = sum(2, 3,2)
print(result)
