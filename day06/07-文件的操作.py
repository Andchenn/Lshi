# 文件的访问模式：
# 1.r：只读，文件不存在会崩溃
# 2.w：只写
# 3.a：追加
# 4.rb:以二进制方式读取文件：常用
# 5.wb:以二进制的方式写入文件：常用
# 6.ab：以二进制的方式追加数据：常用
# r+，w+，a+ 支持读写
# rb+，wb+，ab+ 支持二进制方式读写操作


# 读取文件
# ----------r模式（只读）
# 如果没有此文件会崩溃
# 打开文件解码过程（解析）
file = open("1.txt", "r", encoding="utf-8")
# 读取文件所有的数据
content = file.read()
print(content)
# 关闭文件(必须的)
file.close()

# --------w模式
# w模式，如果文件存在，那么文件中原有数据，会被清空，在写入数据
# 如果文件不存在，会帮助我们创建文件
# 默认编码格式utf-8，windows是gbk
# 为了兼容windows和mac电脑，encoding="utf-8"
file = open("1.txt", "w", encoding="utf-8")
file.write("B")
file.write("B")
file.write("B")
# 查看当前编码格式(cp936)
result = file.encoding
print(result)
# 一般情况不影响，内存泄漏，记住文件的最后一步都是close
file.close()

# ---------------a：追加数据

file = open("1.txt", "a", encoding="utf-8")
file.write("BBB")
file.close()

# ------------rb:以二进制方式读取数据
# binary mode doesn't take an encoding argument
# 如果是二进制方式不需要指定编码格式(帮助我们编码)

file = open("1  .txt", "rb")
file_data = file.read()
# 解码的操作(二进制方式需要解码)
content = file_data.decode("utf-8")
# 不支持写入数据
# file.write("张三")
print(content)

# ------------wb：以二进制方式写入数据
# w模式都会覆盖原来的数据
file = open("1.txt", "wb")
# 需要把写入的数据包装成二进制(编码的过程)
content = "hello"
# 写入二进制数据需要编码
file_data = content.encode('utf-8')
file.write(file_data)
file.close()

# ------------ab：以二进制追加数据

file = open("1.txt", "ab")
# 编码
content = "哈哈"
file_data = content.encode("utf-8")
file.write(file_data)
file.close()

# ---------------r+:支持读写
# 为了兼容不同的操作系统，只要没有看到b就使用encoding
file = open("1.txt", "r+", encoding="utf-8")
file.write("abc")
result = file.read()
print(result)
file.close()
