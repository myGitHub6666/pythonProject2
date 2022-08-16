# 找出传入列表或者元祖的奇数位对应的元素，并返回一个新的列表
def func(con):
    """
    :param con:
    :return:
    """
    new_list = []
    # for i in con[1::2]: 偶数位的元素
    for i in con[::2]:
        # print(i)
        new_list.append(i)
        # print(new_list)
    return new_list


print(func([1,3,4,5,6,78,9,0,2]))
print(func((1,4,6,88)))



