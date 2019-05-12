# 类的名字命名规则见名知意
class AA(object):
    # 复写父类的方法
    def __init__(self, name):
        print("AA")
        self.name = name


class BB(AA):
    # 提示一下：如果子类复写了父类的方法，那么不会执行父类的方法
    def __init__(self):
        # 调用父类的init方法（调用本身类的方法）
        # self.__init__("张山")
        # 使用类名(注意点必须传入对象)
        # AA.__init__(self, "张三")
        # print("BB")
        # 类继承链的方法
        # super().__相当于super(BB,self)
        # 如果不传参数，代用当前的下一个类 ，当前链条
        super(BB,self).__init__("张三")
        print(self.__class__.mro())


b = BB()
print(b.name)
