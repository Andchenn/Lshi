# 自定义模块：程序员自己创建的模块
# 模块的命名规则：和变量命名规则一样
# 1.不可以以数字开头，可以字母 _

# 导入模块(将所有的代码赋值过来)

import day09.first_model

import day09.second_model

# 可能模块里面的代码
# 模块名.变量  模块名.函数名
print(day09.first_model.g_num)

day09.first_model.show()

stu = day09.first_model.Student("李四", 18)
stu.show()

result=day09.second_model.sum_num(20,10)
# 打印当前模块（主模块）
print(result)
