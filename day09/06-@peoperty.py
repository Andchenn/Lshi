class Student(object):
    def __init__(self):
        self.__score = 100

    # 将方法修改成对象的属性值
    @property
    def get_score(self):
        # 类的内部使用私有属性
        # 返回私有属性
        return self.__score

    @get_score.setter
    # 根据你传入的参数
    # 设置私有属性值
    def set_score(self, score):
        self.__score = score


stu = Student()
# 在外部可以修改私有属性（不建议使用）
# stu.set_score(99)
# value=stu.get_score()
# print(value)

stu.set_score = 99
value=stu.get_score
print(value)