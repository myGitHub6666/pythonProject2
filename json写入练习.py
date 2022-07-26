# 文件对象.write(字符串)不能将python中的列表和字典作为参数传递。想要将python中的数据类型存为json文件，需要使用json
# 提供的方法，不再使用write。
# 步骤 导包，写方式打开文件。写入 json.dump(python中的数据类型，文件对象)
import json

my_list = [('admin', '123456', '登录成功'), ('root', '123456', '登录失败'), ('admin', '123123', '登录失败')]
with open('json_01.json', 'w', encoding='utf-8') as f:
    # my_list中的数据写到json——01的文件中去。
    # json.dump(my_list, f) 不写这个就是默认是ascii码的形式展示
    # 缩进2，显示正常中文。
    json.dump(my_list, f, ensure_ascii=False, indent=2)
