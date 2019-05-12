my_list = [1, 2, 3, 4]
my_tuple = (5, 6)
my_set = {5, 9}

# 把列表转换成集合(集合不允许有重复数据，转换会去重)
result = set(my_list)
print(result)

# 元组转换集合
result = set(my_tuple)
print(result)

# 把列表转换成元组
result = tuple(my_list)
print(result)

# 把集合转为元组
result = tuple(my_set)
print(result)

# 把元组转为列表
result = list(my_tuple)
print(result)

# 把集合转成列表
result = list(my_set)
print(result)

#list()转换成列表
#tuple()转换成元组
#set()转换成集合