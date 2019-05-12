# 定义一个全局变量
g_num = 10


# 定义函数
def show():
    print("我是函数")


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)
