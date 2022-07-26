import json
import unittest
from parameterized import parameterized
from tools_01 import login


# 必须把数据转化为[[],[],[]]形式或者[(),(),()]
def build_date():
    with open('data.json', encoding='utf-8') as f:
        res = json.load(f)
        data = []
        for i in res:
            data.append((i.get('username'), i.get('password'), i.get('expect')))
    return data  # 测试数据是正常的


# 定义测试类
class TestLogin(unittest.TestCase):
    # 组织测试数据并传参
    @parameterized.expand(build_date()) # 把测试数据加入到这个参数中，依次进行传参
    def test_login(self, username, password, expect):
        self.assertEqual(expect, login(username, password))

