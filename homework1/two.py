# 字典中通过键获取值的两种方式及比较a={'a':'a','b':'b'}


a = {'a': 'a', 'b': 'b'}
a1 = a['a']
b1 = a['b']
print(a1, b1)
print(list(a.values()))
print(list(a.items()))
