class Animal(object):
    # 对象方法(需要有对象才可以调用)
    def run(self):
        print("动物跑起来了")


class Dog(Animal):
    # 可以调用父类的方法(但是子类重写父类的方法，会调用自身，死循环)
    def run(self):
        # 调用父类的方法(不建议使用)
        # self.run()
        # 使用类名去调用父类的方法
        # Animal.run(self)
        # Dog表示类继承链的下一个类（指定的继承链中指定类的下一个类）
        # self 表示当前类的继承链(指定的继承链)
        super(Dog,self).run()
        # 打印类的继承链
        print(self.__class__.mro())

    def wang(self):
        print("汪")


dog = Dog()
dog.run()
