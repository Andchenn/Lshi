# if :bool 类型，数字类型
if True:
    print("条件成立")
# 数字类型：非0即真(只要不是0就满足条件)
if 1:
    print("条件成立")

# if 容器类型(字符串，列表，元组，字典，集合，二进制数据)
# 容器类型判断的时候，如果容器类型里面有数据那么表示条件成立，否则条件不成立

if "xx":
    print("哈哈")

if [1,2]:
    print("呵呵")

if (1,2):
    print("hhh")

if {"a":1,"b":2}:
    print("jjj")

# 非None条件成立
if not None:
    print("none")