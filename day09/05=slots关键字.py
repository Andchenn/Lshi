# 指明创建对象的时候不能增加其他属性


class Student(object):
    # 这样的操作会固定属性
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student("ss", 15)
# 动态添加一个属性
# stu.sex="男"
# 修改属性
stu.name = "李四"
print(stu.name)
