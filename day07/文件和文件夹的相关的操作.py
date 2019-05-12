import os

file = open("4.txt", "w", encoding="utf-8")
file.write("abc")
file.close()

# 修改文件的名字，如果文件不存在会报错
os.rename("4.txt", "3.txt")

# 创建文件夹(已经存在A的名字，继续创建会报错)
# 在当前路径下创建(默认路径是pycharm的路径)
os.mkdir("A")
# 给文件夹改名字(目标文件不存在会报错)
os.rename("A", "B")
# 指定路径创建文件


# 查看当前目录的路径
current_path = os.getcwd()
print(current_path)
# 创建指定路径下的文件
file = open("B/4.txt", "w", encoding="utf-8")

# 切换到指定路径
os.chdir("B")
current_path = os.getcwd()
print(current_path)

# 创建文件
file = open("10.txt", "w", encoding="utf-8")
file.close()

# 删除文件(文件夹中有文件不可以删除)
os.remove("B")
# 删除文件夹中的文件
os.remove("B/4.txt")
# 删除文件夹(文件夹中还有文件)
import shutil
#删除文件树
shutil.rmtree("B")

