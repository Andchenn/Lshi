# for循环最经常使用的方式就是遍历(所有容器类型)
# 获取所有容器类型里面的元素，就是遍历(字符串，列表，元组，字典，集合)

# 字符串
str = "abc"
for value in str:
    print(value)

# 列表
my_list = ["苹果", "雪梨"]
for value in my_list:
    print(value)

# 把列表当中的元素都遍历出来，还想对应的下标
my_list = enumerate(["苹果", "草莓"])
# print(type(my_list))
#
# for value in my_list:
#     print(value,type(value))

# 拆包：获取容器类型中所有元素和所有下标
for index, value in my_list:
    print(index, value)

# 元组
for value in enumerate((1, 5)):
    print(value)

# 字典遍历
my_dict = {"name": "张三", "age": 6}
# 遍历(默认遍历出来的是key)
for key in my_dict:
    print(key)

# 遍历value
for value in my_dict.values():
    print(value)

# 将key和value全部都遍历出来
for key, value in {"name": "张三", "age": 6}.items():
    print(key, value)

# 集合
my_set = {1, 3, 5}
for value in my_set:
    print(value)
