# 检查传入字典的每一个value的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回给调用的函数
def func(dic):
    """

    :return:
    """
    for i in dic.values():
        # print(i)
        if len(i) >= 2:
            return i[0:2]
        else:
            return None


dict1 = {"name": "xiaoming", "city": "chengdu"}
print(func(dict1))
