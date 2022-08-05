i = 1
mylist = []
while i < 10:
    print(f"top i is {i}")
    mylist.append(i)
    print(mylist)
    i += 1
    print(f"bottom i is {i}")
# 打印整个列表
print(f"mylist is {mylist}")
# 获取列表中的每个值
print('this mylist is:', end=" ")
for i in mylist:
    print(i, end=" ")


