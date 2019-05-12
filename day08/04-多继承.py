# 多继承：相当于多个父亲

class A(object):
    def show(self):
        print("我是A类")


class B(object):
    def show(self):
        print("我是B类")


class C(A, B):
    pass


c = C()
# 调用父类的方法
# 类的继承顺序，决定方向调用的时候查找的顺序
print(C.mro())

c.show()
