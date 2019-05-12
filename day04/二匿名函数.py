# 匿名函数：没有名字的函数就是匿名函数
# lambda：这个关键字修饰的就是匿名函数
# 匿名函数的应用场景：简化代码
def sum(a, b):
    result = a + b
    return result


result = sum(1, 2)
print(result)

# 匿名函数的第一种写法
result = (lambda x, y: x + y)(1, 2)
print(result)

# func是匿名函数的函数名字
# 系统给我们的方法(返回给我们一个函数)
func = lambda x, y: x * y
result = func(1, 6)
print(result)


# 判断你传入的是否是偶数
def is_os(num):
    if num % 2 == 0:
        return True
    else:
        return False


result = is_os(1)
print(result)

# 返回一个函数，我们用变量来承接它
new_func = lambda num: True if num % 2 == 0 else False
result = new_func(2)
print(result)

my_list = [2, 5, 1]
# 对列表进行排序(默认从小到大排序)
# reverse=True从大到小排序
my_list.sort()
print(my_list)

my_list = [{"name": "lili", "age": 20}, {"name": "lisi", "age": 19}]
# key=函数
my_list.sort(key=lambda item: item["age"])

print(my_list)


# 正常使用的函数
def get_value(item):
    return item["age"]


# 默认从小到大
my_list.sort(key=get_value, reverse=True)
print(my_list)
