# 魔法方法：当前需要完成某个功能的操作的时候会自动调用的方法

# 比如：__init__方法
# 魔法方法的表现形式：__开头，__结尾魔法方法
# init，当前对象初始化的时候调用这个方法
class Teacher(object):
    # init方法里面去给对象添加属性
    # 创建完成对象后，python自行帮助我们调用的方法
    # self 表示当前对象
    def __init__(self, name, age):
        print("这是init的方法")
        print(name, age)

    def show(self):
        print("这是show的方法")


t = Teacher("张三", 15)
t.show()