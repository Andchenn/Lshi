# 循环while循环  for循环：根据条件循环执行某种操作
# 死循环，一直满足条件就死循环(cpu)
# 最常见的Bug之一
# while True:
#     print("hello")

# 执行5次循环
num = 0
while num < 5:
    # 每执行一次，就让num+1
    print(num)
    num += 1

# for 循环，结合range来使用(range代表一个范围)
for value in range(5):
    print(value)

# (0,6,1),起始数据，结束数据(结束数据不执行循环)，步长（跳跃的距离）
for value in range(0, 6, 1):
    print(value)
