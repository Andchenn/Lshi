# 缺省参数：在函数定义的时候参数就有值(默认值)
# 那么这种参数就叫缺省参数
# 如果不给缺省参数的参数传值，，那么使用默认值
# 如果传值，使用新传的值做计算
#num1必选参数
#num2缺省参数
# 提示一下：如果有必选参数和缺省参数，那么缺省参数必须放到必选参数后面
def sum_num(num1=1, num2):
    result = num1 + num2
    return result


value = sum_num(1,6)
print(value)
