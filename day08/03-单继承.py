# 类的三大特性：封装继承多肽
# 继承的好处：子类可以复用父类的属性和方法

class Person(object):
    def __init__(self):
        self.name = "张三"
        self.age = 18

    # 方法
    def show(self):
        print(self.name, self.age)


# 定义一个学生类
class Student(Person):
    def __init__(self):
        self.subject = "数学"

    def show(self):
        print(self.subject)


s = Student()
# 子类调用父类的方法
s.show()
print(s.name, s.age)


def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=", i)
        # 做一些其它的事情
    print("do something.")
    print("end.")


def call(i):
    return i * 2


# 使用for循环
for i in yield_test(5):
    print(i, ",")