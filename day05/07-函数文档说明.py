"""
这是一个多行注释
"""


def sum_num(num1, num2):
    # 一般情况程序员不去写文档说明
    # 第三方公司
    """
    :param num1:第一个数字
    :param num2:第二个数字
    :return:返回值
    """
    return num1 + num2


result = sum_num(1, 2)
print(result)
