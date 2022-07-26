# 书写TestCase代码对add函数进行测试
import unittest

from tools import add

version = 29


# 自定义测试类
class TestCase01(unittest.TestCase):  # 不要忘记写继承的父类
    @unittest.skip('没有什么原因就是不想执行')
    def test_tools1(self):
        if add(1, 2) == 3:
            print("测试正确")
        else:
            print("测试错误")

    def test_tools2(self):
        if add(10, 20) == 30:
            print("测试正确")
        else:
            print("测试错误")

    @unittest.skipIf(version > 30, '版本大于30不用测试')
    def test_tools3(self):
        if add(1, 20) == 30:
            print("测试正确")
        else:
            print("测试错误")
