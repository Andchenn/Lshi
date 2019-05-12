# 递归函数：在函数里面调用函数本身就是递归函数
# 特征1.传递2.回归
# 死循环

# 递归函数：无限递归：默认最多递归1000次
# def show():
#     show()
#
#
# show()


# 不常用

# 阶乘

def calc_num(num):
    # 当计算到1的阶乘的时候直接返回1，跳出这个递归（函数）
    if num == 1:
        return 1
    else:
        return num * calc_num(num - 1)


result = calc_num(5)
print(result)

import sys

# 获取默认递归的次数（默认1000）
result = sys.getrecursionlimit()
print(result)

# 设置递归的次数
sys.setrecursionlimit(1200)
result = sys.getrecursionlimit()
print(result)

result = calc_num(1100)
print(result)
