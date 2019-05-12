# 约定俗成(类名首字母大写)
# class + 类名(继承的父类)
class Teacher(object):
    # 方法（谁调用谁就是self）
    def show(self):
        print("今天天气很好")


t = Teacher()
# 在外部添加属性(动态添加)
t.name = "李四"
t.age = "18"

# 获取对象的属性
print(t.name, t.age)
t.show()
