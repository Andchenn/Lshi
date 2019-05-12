# continue:结束本次循环 然后继续下一个循环，整个循环不一定结束

num = 0
while num < 5:
    num += 1
    if num == 2:
        continue
    print(num)
else:
    print("结束循环")

# break :跳出整个循环(结束)
print("--------------")
num = 0
while num < 5:
    num += 1
    if num == 2:
        break
    print(num)
else:
    # 注意：break，会不执行else的代码
    print("结束循环")

print("--------------")

for value in range(1, 5):
    if value == 2:
        break
    print(value)
else:
    print("结束循环")

# 总结：不可以单独使用break和contine,必须结合循环使用