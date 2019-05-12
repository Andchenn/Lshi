import json

# 数据格式json（解析json）xml
# 只支持部分数据类型（列表字典，int...）
# 序列化自定义类型
my_list = [{"name": "张三", "age": "20"}]
file = open("mylist1.txt", "w", encoding="utf-8")

# 序列化
json.dump(my_list, file)
file.close()

# 反序列化
file = open("mylist1.txt", "r", encoding="utf-8")
my_list = json.load(file)
print(my_list)
file.close()


# 自定义类型
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 序列化
stu = Student("张三", "52")
file = open("stu.txt", "w", encoding="utf-8")
# 序列化对象，本质上就是把对象的属性进行保存
json.dump(stu.__dict__, file)
print(stu.__dict__)
# file.close()
#
# # 反序列化
file = open("stu.txt", "r", encoding="utf-8")
stu = json.load(file)
print(stu)
