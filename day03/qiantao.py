# 函数嵌套：在函数里面定义一个函数

def call_able():
    # 函数内的函数不能在外部使用
    def text():
        print("我的嵌套函数")

    # text()
    return text


result = call_able()
result()
