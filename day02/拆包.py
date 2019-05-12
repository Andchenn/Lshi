# 拆包：通俗理解，就是把容器类型(字符串，列表，元组，字典，集合)
# 每个数据都用变量保存一下
# 字符串
my_str = "abc"
a, b, c = my_str
print(a, b, c)
# 列表
my_list = [1, 5]
num1, num2 = my_list
print(num1, num2)

# 元组
my_tuple = (1, 5)
num1, num2 = my_tuple
print(num1, num2)

# 拆字典（默认的是key）
my_dist = {"name": "张三", "age": "18"}.values()
a, b = my_dist
print(a, b)

# 集合
my_set = {1, 3}
num1, num2 = my_set
print(num1, num2)
