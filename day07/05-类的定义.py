# 类的定义，使用class关键字 创建的（特征和属性）
# 类有属性(特征)和方法(行为)

# 定义老师类
# 旧式类的创建方法
# 创建一个Teacher的类继承object
class Teacher():
    # 属性(国籍)
    country = "中国"

    # 方法
    def show(self):
        print("我是大家的授课老师")


# 类图纸，对象是根据图纸绘制出来的
# 通过类创建对象(在内存中开辟了一块空间，空间存的是对象的内存地址)
teacher = Teacher()
teacher1 = Teacher()
# 通过对象查看属性
print(teacher.country)
# 通过对象调用方法
teacher.show()

print(Teacher.__bases__)
