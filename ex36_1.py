# 如果输入的用户名==“小新”，则继续输入密码。如果不等于就重新输入。
# 然后再输入密码， 如果密码等于123456则通过，否则重新输入。
while True:
    name = input("> ")
    if name == "小新":
        break
    else:
        print("请重新输入")
        continue

while True:
    password = input(">")
    if password == "12346":
        break
    else:
        print("请重新输入密码")
        continue
