class Person(object):
    def show(self):
        print("我是人类")


class Plane(object):
    def show(self):
        print("我是飞机")

    def fly(self):
        print("飞机起飞了")


class Student(Person, Plane):
    def show(self):
        # 调用父类的方法
        super(Student, self).show()
        super(Person, self).show()
        print(self.__class__.mro())


s = Student()
s.show()
