# 格式化符号：%s,%d,%f,%x
# %s:输出字符串
# %f：输出float类型
# %d输出int类型
# %x：输出16进制的类型

name = "小明"
print("我叫%s" % name)

score = 100
print("我的成绩是%d" % score)

pi = 3.1415926
# %f默认保留6位小数，会四舍五入
print("圆周率%.2f" % pi)

num = 16
print("%x" % num)
