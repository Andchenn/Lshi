# __del__:对象释放的时候会自动调用魔法方法
# 1.程序退出，程序中所有的对象都会销毁

import time


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 当对象的引用计数为0的时候会调用此方法
    def __del__(self):
        print("对象被销毁了")


# 在内存开辟了一块空间（ffc0）
# 引用计数0-1
xiao_ming = Person("张三", 20)
# 1-2
xiao_lan = xiao_ming
# 手动的干掉小明对象(删除对象)
# 减去一个引用计数2-1
del xiao_ming
# 引用计数：内存地址的使用次数
time.sleep(3)
print("程序退出了")
