# 1.打开源文件读取数据
src_file = open("1.txt", "rb")
# 指定写入的路径
dst_file = open("5.txt", "wb")
# 读取
while True:
    file_data = src_file.read(1024)
    # 判断文件是否读取完毕
    # 写入数据了
    if file_data:
        dst_file.write(file_data)
    else:
        print("数据读取完成了")
        # 没有数据了就不需要读取，也不需要写入
        break

src_file.close()
dst_file.close()
