"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
"""

import time
import math

start = time.clock()
for i in range(1, 10000):
    sum = 0
    for factor in range(1, int(math.sqrt(i)) + 1):
        if i % factor == 0:
            sum += factor
            if 1 < factor != i / factor:
                sum += i / factor
    if sum == i:
        print(i)
end = time.clock()
print("执行时间：", (end - start), "秒")
