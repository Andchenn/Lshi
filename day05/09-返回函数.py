# 在函数内部返回一个函数，返回的这个函数就是返回函数

# 函数嵌套

def show():
    def show1():
        print("今天天气很冷")

    return show1


# newfunc就是show1
new_func = show()
new_func()


# 返回函数也是高阶函数的一种
# 根据传入的不同参数，返回不同的函数(返回函数的重要意义所在)


def calc(operation):
    if operation == "+":
        def sun_num(num1, num2):
            result = num1 + num2
            return result

        # 返回函数就不需要加(),加()就等于调用函数
        return sun_num

    if operation == "-":
        def jq_num(num1, num2):
            return num1 - num2

        return jq_num


new_func = calc("-")
print(new_func)
# 相当于调用sum_num
result = new_func(1, 2)
print(result)


def sum_num(num1, num2):
    result1 = num1 + num2
    result2 = num1 - num2
    return result1, result2


value = sum_num(2, 2)
# 多个返回值，包装成一个元组
print(value)
