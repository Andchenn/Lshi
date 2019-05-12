# 练习1
# 判断下列选项调用函数正确与否，并给予说明
# A:abs() B:abs(-1,4) C:abs(-1,-3) D:abs('a)
# 注：abs()绝对值函数，可以百度查询相关规则


# 练习2
# 定义一个函数，输入不定个数的数字，返回所有数字的和
def sum(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

def sum(**kwargs):
    sum = 0
    for n in kwargs.values():
        sum += n
    print(sum)

# sum(2, 4)
sum(a=1,b=2)

# 练习3
# (传入不定长参数返回计算结果，使用不定长位置参数和关键字参数两种方式)
# 定义一个函数，内置求和函数sum()


# 练习4
# 编写一个函数，输入n的偶数时，调用函数求1/2+1/4+...+1/n，当输入n为奇数时，调用1/1+1/3+...+1/n