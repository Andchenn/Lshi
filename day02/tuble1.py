# 元组：以小括号形式的数据结合，（1,2,“abc”，Ture）
# 可以存储任意数据类型
# 注意：元组可以根据下标获取数据，但是不能对元组进行数据修改

my_tuple = (1, 4, "abc", True, 1.2)
print(my_tuple, type(my_tuple))

# 根据下标取值
value = my_tuple[-1]
print(value)

# 元组不能根据下标删除数据
# del my_tuple[2]
# print(my_tuple)

# 修改数据
# my_tuple[0] = 3
# print(my_tuple)

# 注意不论元组里面装什么数据类型都不能修改
my_tuple = (1, [2, 3])
# my_tuple[1] = [2, 3]
my_list = my_tuple[1]
my_list[0] = 5
print(my_list)
my_list = [1, 2]
print(my_tuple)

# 定义一个空的元组
# 坑：如果定义的元组，只有一个元素，那么元组的类型为元素的类型
# 如果指定只传一个元素，还想保证是元组类型，那么需要加上逗号
my_tuple = (1,)
print(my_tuple, type(my_tuple))

# 判断数据是否正在元组里面
my_tuple = (10, 5, 10, 10)
result = 5 in my_tuple
print(result)

result = 3 not in my_tuple
print(result)

# 元组中的元素的下标(字符串，列表，元组都是有下标的，有序的)
result = my_tuple.index(5)
print(result)

# 元组中元素的个数
result = my_tuple.count(10)
print(result)
