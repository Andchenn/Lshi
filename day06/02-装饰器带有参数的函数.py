# 定义一个装饰器


def decorator(func):
    def inner(num1,num2):
        print("计算结果如下：")
        # 调用的时候要知道真正调用的是哪个函数
        func(num1,num2)
    return inner

@decorator
# 定义一个带有参数的函数，装饰器装修他
def num_sum(num1,num2):
    result= num1+num2
    print(result)

num_sum(2,5)