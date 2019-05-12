# 注意点：*后面的参数，必须使用关键字传参方式
def callAble(address, sex, *, name, age):
    print(address, sex, name, age)


# 使用位置传参的方式调用函数
callAble("广州", "男", name="lili", age=20)
