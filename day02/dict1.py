# 字典：以大括号形式的键值对数据组合，{“name”：“张三”，“age”:18}
# 提示一下：一般key(99% 都是字符串类型)
# 不可变类型：数字 元组 可变类型：变量 列表
my_dict = {"name": "张三", "age": 18}
print(my_dict, type(my_dict))

# 字典是无序的(没有下标的概念)
# 通过key值来取vaule
vaule = my_dict["name"]
print(vaule)
# 如果没有此键，使用[]会崩溃
# vaule = my_dict["sex"]
# print(vaule)

# 如果使用get方式取值不会崩溃，会返回None
# get也可以设置字典的默认值，增加了一个元素
result = my_dict.get("sex", "男")
print(result)
