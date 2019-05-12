# 集合：以大括号形式表现的数据集合，集合里面的数据不可以重复
# 集合可以根据下标获取数据，也可以添加和删除
# 不可以以此种方式定义空的集合
# my_set = {} #dict字典

my_set = {1, 4, "abc", "张三"}
print(my_set)

# 删除数据(删除指定数据)(不能删除没有的数据)
# my_set.remove("22")
# print(my_set)

# 增加数据
# 不可以添加重复的数据
my_set.add("5")
my_set.add("5")
my_set.add("5")
print(my_set)

# 删除集合里面的数据(删除没有的数据不会崩溃)
# my_set.discard(12222)
# print(my_set)

# 根据下标修改数据(集合是无序的)
# my_set[0] = 2
# print(my_set)

# 取出数据容器里面的每一个元素，就是遍历
for value in my_set:
    print(value)

# 定义一个空集合
my_set = set()
print(my_set, type(my_set))

my_set.add("a")
my_set.add(123)
my_set.add(11)
print(my_set)

# 作业：
# 将集合转换成列表，元组（三种数据容器类型相互转换）
# tuple()   list()  set()
