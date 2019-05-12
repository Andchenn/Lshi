# 内置函数：可以直接使用的函数(不用自己声明，python已经定义好了)
# print.len,max,min,sort,sorted,open
# api(接口)
# len 可以统计容器类型的长度(个数)(字符串,列表，元组，字典，集合)
# 统计字符串的个数

str = "abc"
result = len(str)
print(result)

# 列表
result = len([1, 2])
print(result)

# 字典
result = len({"a": "b"})
print(result)

# 元组
result = len((1, 2, 3))
print(result)

# 集合
result = len({1, "b"})
print(result)

# max函数 统计容器类型数据中的最大值
result = max("12345")
print(result)

# 列表
result = max([1, 2, 3])
print(result)

# min统计容器类型数据中的最小值
result = min([100, 200, 20])
print(result)

# 列表排序(会返回一个新的列表)
new_list = sorted([9, 8, 12], reverse=True)
print(new_list)

# 删除变量
del new_list
# print(new_list)
