# 练习1
# 创建两个列表，列表1含有字符串’life','is','short',列表2含有字符串'you','need','python'.并输出‘need’

list1 = ['life', 'is', 'short']
list2 = ['you', 'need', 'python']
print(list2[1])

# 练习2
# 截取列表['a','b','c','d']中的前三个元素

my_list = ['a', 'b', 'c', 'd']
list = my_list[0:3:1]
print(list)

# 练习3
# 对已给字典dict={'Name':'Zara','Age':7,'Class':'First'},
# 增加Age=8与School=DPS School 两键值对、并输出。
# 向字典添加新内容的方法是增加新的键/值对  修改或删除已有键/值对如下：
# 输出结果样例为：
# dict['Age']:8
# dict['school']:DPS School

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict["Age"] = 8
dict["School"] = "DPS School"
print("dict['Age']:", dict["Age"])
print("dict['School']", dict["School"])

# 练习4
# 用while...else...语句编写一个程序，判断输入数字是奇数还是偶数

num = int(input("请输入一个数："))
while num % 2 == 0:
    print("是偶数")
    break
else:
    print("是奇数")

# 练习5
# 用continue语句作为循环控制语句 输出1-100以内的偶数
for num in range(0, 101):
    if num % 2 > 0:
        continue
    print(num)
