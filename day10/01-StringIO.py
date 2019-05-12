# 将字符串写入内存
import io

# String IO操作和文件的写入读取很像

str_io = io.StringIO()

# 向内存写入数据
str_io.write("hello")  # 5
str_io.write("world")  # 10

# 读取内存中的数据
content = str_io.getvalue()
print(content)
# 文件的指针（从10开始读）
# 设置文件指针到文件开头
str_io.seek(0)
# 默认全部读取
result = str_io.read()
print(result)

