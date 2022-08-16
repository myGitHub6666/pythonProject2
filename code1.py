# 接收n个数字，求N个数字的和
def sum(*args):
    """
    *args可以接收不定长的可变参数.
    :return:
    """
    result = 0
    for i in args:
        result += i
    return result


print(sum(1,3,3))
print(sum(2,4,6,8,9))




