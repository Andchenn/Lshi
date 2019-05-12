# new:当前对象创建的时候就会调用
# init方法：当对象创建完毕调用init方法，给对象添加属性及其初始化
# 创建对象的时候调用两个方法，先调用new，new调用完毕之后，表示对象创建完毕
# 然后调用init方法实例化


class Student(object):
    def __new__(cls, *args):
        print("创建了对象")
        print(args)
        # 必须返回父类的new方法（调用父类的方法）
        # new方法必须返回（相当创建对象）
        return object.__new__(cls)

    def __init__(self, age, name):
        print("初始化")
        self.age = age
        self.name = name


stu1 = Student(15, "小麦")
stu2 = Student(16, "小草")
print(id(stu1))
print(id(stu2))
