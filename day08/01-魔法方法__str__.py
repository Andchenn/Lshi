# __str__:当前用print函数打印对象的时候会调用此方法
class Person(object):
    def __init__(self, name, age):
        # 在init方法里面定义的属性就是实例属性
        self.name = name
        self.age = age

    # 魔法方法str
    def __str__(self):
        # 返回一个字符串信息
        return "我叫：%s 年龄：%d" % (self.name, self.age)


person = Person("张三", 18)
print(person)
# 内存地址
print(id(person))
# 访问对象的实例属性
print(person.name)
print(person.age)
