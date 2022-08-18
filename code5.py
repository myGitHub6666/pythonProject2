# 求三组连续自然数的和：求出1到10，20到30,30到45的和
def sumCount(a, b):
    # sum(range(a,b+1))
    return sum(range(a, b + 1))


print(sumCount(1, 10))
print(sumCount(20, 30))
print(sumCount(30, 45))
print("*" * 100)


# 100个和尚吃100个馒头。一个大和尚吃3个馒头，三个小和尚吃一个馒头。问大和尚和小和尚分别有多少
def peopleCount():
    """
    大和尚为a，小和尚为100-a
    :return: 返回a，100-a
    """
    for a in range(0, 101):
        if 3 * a + (100 - a) * (1 / 3) == 100:
            return a,(100 - a)


print(peopleCount())

# 指定一个列表，列表中含有唯一一个只出现过一次的数字，写程序找出这个独一无二的数字
