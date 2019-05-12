# 1.打开源文件读取数据
# rb比较通用的原因是兼容不同的数据，文件图片视频，都可以.

src_file = open("1.txt", "rb")
# 2.读取（大数据量不行）
file_data = src_file.read()
# 打开目标文件，写入数据
# 写入pychram
dst_file = open("5.txt", "wb")
# 把源文件内容写入到目标文件里面
dst_file.write(file_data)
# 关闭文件
dst_file.close()
src_file.close()
