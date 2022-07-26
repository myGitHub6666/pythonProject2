# 断言的结果，有两种，TRUE代表通过，FALSE代表代码抛出异常，用例不通过
# 在unittest中使用断言，都要通过self。断言方法 来试验
# self.assertEqual（预期结果，实际结果）。这个是用来判断预期结果和实际结果是否相等
# 如果相等，用例通过，如果不相等，抛出异常，用例不通过
# self.assertIn(预期结果，实际结果）判断预期结果是否在实际结果中，包含的话，用例通过，不包含，用例抛出异常，用例不通过
# assertIn('admin','admin') 包含
# assertIn('admin',"adminnnnn") 包含
# assertIn('admin','aaaadmin')包含
# assertIn('admin','aaaadminnnn')包含
# assertIn('admin','adddminnn') # 不包含
import unittest
from tools_01 import login


class TestLogin(unittest.TestCase):
    def test1(self):
        self.assertEqual('登录成功', login('admin', '123456'))  # 对比两个的值是否相等

    def test2(self):
        self.assertEqual('登录失败',login('admin', '123123'))

    def test3(self):
        self.assertEqual('登录失败',login('root', '1234'))
        self.assertIn('失败',login('root', '123'))
