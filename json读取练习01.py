# 需求，提取json文件中的用户名，密码，和预期结果，组成如下格式[(),(),()](这是自动化参数化需要的数据格式)
import json

list1 = []  # 列表中添加数据


def getjson():
    with open('data.json', encoding="utf-8") as f:
        buf = json.load(f)  # buf是列表类型
        # print(buf)
        for user in buf:
            # append后面是填入的数据。 向列表中添加元组
            list1.append((user.get('username'), user.get("password"), user.get("expect")))
    return list1


print(getjson())
