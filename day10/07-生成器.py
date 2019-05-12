# 生成器：就是一个特殊的迭代器，他同样可以通过next函数和for循环取值

# 列表生成器
result = [x for x in range(4)]
print(result)
# 生成一个生成器
result = (x for x in range(4))
print(result, type(result))

# 测试一下：是next获取下一个值
# value=next(result)
# print(value)

# for 循环遍历生成器，自动停止迭代
for value in result:
    print(value)

print('---------------------------')
# 2.使用yield创建生成器
def show_num():
    for i in range(5):
        # yield 代码遇到它会暂停，然后把结果返回过去
        # 下次启动的时候，生成器会在暂时的位置
        # yield 特点：可以返回多次值，return只能返回一次
        yield i


result = show_num()
# print(result)
# 迭代器也是生成器，可以直接遍历
for value in result:
    print(value)
