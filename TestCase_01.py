"""
学习TestCase(测试用例）模块的书写方法
"""
# 1 导包
import unittest


# 自定义测试类，需要继承unittest中的TestCase类即可
class TestCaseDemo1(unittest.TestCase):
    # 书写测试方法，即用例代码，目前没有代码用print代替
    def test_method1(self):
        print("测试方法1-1")

    def test_method2(self):
        print("测试方法1-2")


# 把光标放在class最后就可以执行全部方法
