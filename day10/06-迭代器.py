# 在类里面有一个__iter__方法和__next__这个方法创建的对象就是迭代器
# 作用：根据数据的位置获取下一个位置的值
# my_list=["1","2","3"]
# 用迭代器的好处是及其节省内存
from collections import Iterable


class MyIterable(object):
    def __init__(self):
        self.mylist = [4, 5, 9]
        self.current_index = 0

    def __iter__(self):
        # 返回的是可迭代对象
        return self

    def __next__(self):
        if self.current_index < len(self.mylist):
            # 获取迭代器中的下一个值
            result = self.mylist[self.current_index]
            self.current_index += 1
            return result
        else:
            # 抛出异常，停止迭代
            raise StopIteration


my_iterable = MyIterable()
# result = isinstance(my_iterable, Iterable)
result=iter(my_iterable)
print(result)
# 使用迭代器获取迭代器中的下一个值
# result = next(my_iterable)
# print(result)
# result = next(my_iterable)
# print(result)
# result = next(my_iterable)
# print(result)

for value in my_iterable:
    print(value)