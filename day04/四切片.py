# 切片：根据下标的方位获取一部分数据：字符串，列表
my_str = "hello"
result = my_str[0]
print(result)

# range()
# 起始函数，结束函数(结束数据不)，步长
result = my_str[0:3:1]
print(result)

# 截取前三个数据(默认步长0)
result = my_str[0:3]
print(result)

# 可以省略前面两个(默认从0开始，取到最后一个)
result = my_str[::3]
print(result)

# my_str = "hello"
result = my_str[:]
print(result)

# 获取最后三个元素
result = my_str[-3:]
print(result)

result=my_str[-5:-2]
print(result)