# 自定义异常必须继承Exception


class CustomException(Exception):
    def __init__(self, content):
        self.content = content

    # 表示抛出异常类的描述信息
    def __str__(self):
        return "我是自定义异常"


content = input("请输入数据")
if content != "a":
    # 抛出自定义异常类
    # raise 只是抛出异常类型
    raise CustomException(content)
    # 可以抛出系统异常类型
    # raise NameError("抛出系统类的异常"