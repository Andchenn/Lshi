# 可变类型：可以在原有的数据基础上对数据进行修改(增删改查)
# 不可变类型：不能在原有基础上对数据进行修改
# 可变类型“列表，集合，字典，对数据进行修改后，内存地址不会改变”
# 不可变类型：字符串，数字，元组，不能再原有的数据上对数据进行修改

# 列表
my_list = [1, 5, 6]
print(my_list, id(my_list))
# 改变：增值
my_list[0] = 2
my_list.append(10)
del my_list[1]
print(my_list, id(my_list))

# 字典
my_dict = {"name": "李四", "age": 15}
print(my_dict, id(my_dict))
my_dict["name"] = "张三"
print(my_dict, id(my_dict))

# 集合
my_set = {1, 2, 5}
print(my_set, id(my_set))
my_set.add(7)
print(my_set, id(my_set))

# 不可变类型的操作-----------------------

my_str = "hello"
print(id(my_str))
# my_str[0]="l"
# print(id(my_str))

# 不属于修改数据(重新赋值)
my_str = "haha"
print(id(my_str))

# 数字类型
my_num = 5
print(id(my_num))
my_num = 10
print(id(my_num))

# 元组
my_tuple = (4, 6)
print(id(my_tuple))
# my_tuple[0] = 2
# print(id(my_tuple))

# 这不叫做修改数据，重新赋值，只要重新赋值，任何类型地址都会改变
my_list = [10, 20]
print(id(my_list))
my_list = [20, 30]
print(id(my_list))

#总结：可变类型：可以原有基础数据上修改（内存地址不会发生改变）
