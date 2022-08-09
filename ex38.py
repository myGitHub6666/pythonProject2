ten_things = "Apples orange crows telephone light sugar"

print("wait there are not 10 things in that lists. let's fix that")
# 把字符串转化为列表（用空格把字符串分割成列表形式）
stuff = ten_things.split(' ')
print("<<<<",stuff)
more_stuff = ["day","night", "song", "frisbee", "corn","banana", "girl","boy"]
# 判断这个列表的长度是否为10.如果不是10，一直进行循环
while len(stuff) != 10:
    # 在另一个列表当中去取出元素。默认取出的是最后一个数据boy。因为是后进去的先取出。
    next_one = more_stuff.pop()
    print(f"adding:{next_one}")     # 打印出添加的元素
    stuff.append(next_one)  # 把取出来的元素添加到stuff列表中
    print(f"there are {len(stuff)} items now")  # 打印出现在的stuff的长度
    # 继续循环进行判断。len(stuff)==10就退出循环

print("there we go :", stuff)

print("let's do some things with stuff")
print("<<<<",more_stuff)
# 打印出下标为1的数据
print(stuff[1])
# 打印出下标为-1的数据
print(stuff[-1])
# 获取最后一个数据。
print(stuff.pop())
# 打印下标为0的数据
print(stuff.pop(0))
# 打印下标为-1的数据
print(stuff.pop(-1))
# 把列表转化为字符串
print(' '.join(stuff))
# 从列表下标为3的地方开始取值，直到索引为5，但是5的下标的值无法取到，类似于range(3,5)
print(stuff[3:5])
# 取出来的值用#相隔。
print('#'.join(stuff[3:5]))
