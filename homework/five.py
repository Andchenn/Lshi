# 有1,2,3,4个数字，能组成多少个互补相同且不重复数字的三位数？都是多少？


count = 0
for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if x != y and x != z and y != z:
                count += 1
                print(x, y, z, sep='')

print('可以组成%d位' % count)

def Num():
    count = 0
    nums = []
    for n1 in range(1, 5):
        for n2 in range(1, 5):
            for n3 in range(1, 5):
                if n1 != n2 and n1 != n3 and n2 != n3:
                    num = 100 * n1 + 10 * n2 + n3
                    if nums not in nums:
                        nums.append(num)
                        count += 1
    print(count, nums)


Num()
