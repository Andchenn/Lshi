# 练习1
# 打印单词‘interested’中的每一个字母
for letter in 'interested':
    print(letter)

# 练习2
# 对列表Names={'Bart','Lisa','Adam'}中的每个字打印Hello，xxx
Names = {'Bart', 'Lisa', 'Adam'}
for i in Names:
    print("hello" + ',', i)

# 练习3
# 计算1-100内所有偶数的和（利用循环，预习）
sum = 0
for n in range(0, 101, 2):
    sum += n
print(sum)

# 练习4
# 倒序输出列表[1,2,3,4,5]中的元素
list = [1, 2, 3, 4, 5]
for num in list[::-1]:
    print(num)

# 练习5
# 遍历代码，使用if...elif...else 语句判断输入的一个数字是正数，负数或者零
num = float(input("请输入一个数"))
if num > 0:
    print("正数")
elif num == 0:
    print("0")
else:
    print("负数")

# 练习6
# 根据输入年龄，对其称谓进行归类：大于18岁，输入adult，小于18岁，  输出teenager
# 编写代码，是输出结果为：
# your are is 3
# teenager
age = int(input("请输入你的年龄："))
if age >= 18:
    print("your are is", age)
    print("adult")
else:
    print("your are is", age)
    print("teenager")

# 练习7
# 小明身高1.75,体重80.5kg请根据BMI公式（体重除以身高的平方） 帮助小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻 18.5-25：正常  25-28：过重 28-32：肥胖  高于32：严重肥胖
# 请用代码实现它，并实现输出结果为：
# your bmi is：26.285714285714285
# 过重

height = 1.75
weight = 80.5
bmi = weight / (height * height)
if bmi >= 32:
    print("your bmi is", bmi)
    print("严重肥胖")
elif 28 <= bmi < 32:
    print("your bmi is", bmi)
    print("肥胖")
elif 25 <= bmi < 28:
    print("your bmi is", bmi)
    print("过重")
elif 18.5 <= bmi < 25:
    print("your bmi is", bmi)
    print("正常")
else:
    print("your bmi is", bmi)
    print("过轻")
