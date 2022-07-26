# 导包
# 实例化套件对象
# 使用套件对象添加用例方法
# 实例化运行对象
# 使用运行对象去执行套件对象
import unittest

from TestCase_01 import TestCaseDemo1
from TestCase_02 import TestCaseDemo2

suite = unittest.TestSuite()
# 第一种方法，套件对象.addTest（测试类名（’方法名‘）
# suite.addTest(TestCaseDemo1('test_method1'))
# suite.addTest(TestCaseDemo1('test_method2'))
# suite.addTest(TestCaseDemo2("test_method1"))
# suite.addTest(TestCaseDemo2("test_method2"))
# 第二种方法 套件对象.addTest(unittest.makeSuite(测试类名）），测试类名不能重复
suite.addTest(unittest.makeSuite(TestCaseDemo1))
suite.addTest(unittest.makeSuite(TestCaseDemo2))
# 实例化运行对象
runner = unittest.TextTestRunner()
# 运行对象运行套件对象。输出测试结果
runner.run(suite)