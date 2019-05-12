# 定义一个空的字典
my_dict = {}
print(my_dict, type(my_dict))

# 给字典增加键值对
my_dict["name"] = "张三"
# key是唯一的(如果增加重复，会更新value)
# my_dict["name"]="李四"


my_dict["age"] = 18
my_dict["sex"] = "女"
my_dict["address"] = "上海"
print(my_dict)


# 修改键值对
my_dict["age"] = 66
print(my_dict)

# 删除(删除整个字典)
# a = 10
# del a
# print(a)
# del my_dict
# print(my_dict)

del my_dict["age"]
print(my_dict)
my_dict = {"name": "张三", "age": 18, "sex": "男"}
# 随机删除
# my_dict.popitem()
# print(my_dict)
# 指定数据删除(返回值是删除数据的value)
vaule = my_dict.pop("age")
print(my_dict, vaule)

# 获取所有的value
result = my_dict.values()
print(result)

# 获取所有的key
keys = my_dict.keys()
print(keys)

# 判断key是否在字典里面(不能判断value)
result = "age" in my_dict
print(result)
