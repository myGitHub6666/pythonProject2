# 书写TestCase代码对add函数进行测试
import unittest

from tools import add


# 自定义测试类
class TestCase01(unittest.TestCase): # 不要忘记写继承的父类
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

    def test_tools3(self):
        if add(1, 20) == 30:
            print("测试正确")
        else:
            print("测试错误")
