# 使用for循环和range实现输出1-2+3-4+5-6...+99的和

sum = 0

for i in range(1, 100):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
print(sum)
