def show(name, age, *args, **kwargs):
    print(name, age, args, kwargs)


# 不能使用下列方式调用，因为前面使用了关键字传参，后面不能使用位置传参
# show(name="里斯",age=18,1,4,a=1,b=2)
# show("里斯", 15, 1, 2, 3, 4, a="苹果", b="香蕉")


# 可不可以
def show(*args, name, age, **kwargs):
    print(args, name, age, kwargs)


# kwargs必须放置在后面(不定长关键字参数放置在后面)
show(1, 2, 3, 4, name="lili", age=18, a=1, b=2)
