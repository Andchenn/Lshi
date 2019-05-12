# try:里面代码如果遇见异常，那么不会执行try语句里面的代码

try:
    num1 = int(input("请输入第一个数字"))
    num2 = int(input("请输入第二个数字"))
    result = num1 + num2
    print(result)

# 如果有异常会执行except语句
# e代表异常对象
except ValueError as e:
    print(e)
