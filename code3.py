# 检查传入字典的每一个value的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容保存起来返回给调用函数
def func(dic):
    """

    :return:
    """
    for key,value in dic.items():
        if len(value) >= 2:
            dic[key] = value[0:2]
        else:
            # dic[key] = value  # 写不写这句话好像没区别？？？？
            pass
    return dic


dict1 = {"name": "xiaoming","age":'7899' ,"city": "chengdu"}
print(func(dict1))
