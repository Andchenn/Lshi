# 内置模块：python自己内部的模块：time random
import time
import random

# 随机产生数字（1-5）
result=random.randint(1,5)
print(result)

# 卡住主线程2秒钟
time.sleep(2)
print("hh")