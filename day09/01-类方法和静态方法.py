class Person(object):
    # 私有的类属性
    __type = "黄种人"

    def __init__(self):
        # 实例属性
        self.name = "小红"

    # 定义一个对象方法
    def show(self):
        print("我是对象方法")

    # 定义一个类方法(用关键字classmethod修饰的方法就是类方法)
    @classmethod
    def show_msg(cls):
        print(cls)
        print("我的类方法")

    # 定义一个静态方法
    # 提示一下静态方法和当前对象，还有类没有任何关系
    # 关键staticmethod修饰的方法
    @staticmethod
    def show_static():
        # 一般情况静态方法会使用当前类的逻辑
        # 节省内存
        print("我是静态方法")

    # 类方法的使用场景（修改类属性）
    @classmethod
    def set_type(cls, type):
        # 修改类属性
        cls.__type = type

    @classmethod
    def get_type(cls):
        return cls.__type


# 创建对象，利用对象调用（对象方法，类方法静态方法）
p = Person()
p.show()
# 可以调用类方法
p.show_msg()
# p.show_static()
# 使用类名调用对象方法（需要传入对象）
Person.show(p)
# 使用类名调用类方法
Person.show_msg()
# 使用类名调用静态方法
Person.show_static()
# 使用对象调用静态方法
p.show_static()

# 扩展
# 使用对象调用类方法修改类属性值
p.set_type("黑种人")
result = p.get_type()
# 查看类属性修改成功没有
print(result)
