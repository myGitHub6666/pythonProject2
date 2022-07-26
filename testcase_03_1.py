# 采用测试套件去运行测试用例(testcase_03)
import unittest

from testcase_03 import TestCase01

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestCase01))
runner = unittest.TextTestRunner()
runner.run(suite)
