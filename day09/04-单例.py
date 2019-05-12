# 单例：设计模式 常用设计模式
# 在应用内，不管创建多少次对象，都是同一个对象


class Person(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        # 第一创建对象
        if cls.__instance == None:
            # 创建对象
            print("创建对象 ")
            # 把创建的对象赋值给类属性
            # object.__new__(cls)创建对象
            cls.__instance = object.__new__(cls)
        # 第一次返回的是创建的对象
        # 第二次不满足if判断语句，直接返回类属性（赋值为对象的类属性）
        return cls.__instance

    def __init__(self):
        print("初始化")

    # 不同对象调用show方法会有问不同的实现
    # 相同的对象调用show方法会有相同的实现
    # 数据库(对象去访问数据库)
    def show(self):
        print("这是show方法")


# 多线程，进程，协成

p1 = Person()
p2 = Person()
print(p1, p2)
