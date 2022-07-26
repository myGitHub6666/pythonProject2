import unittest
from HTMLTestRunner import HTMLTestRunner
# testsuite和test-loader 没有自带的测试报告 需要使用第三方的插件
suite = unittest.defaultTestLoader.discover('.', 'testpa.py')
with open('report1.html', 'wb') as f:
    runner = HTMLTestRunner(f, 4, '测试报告', 'python 3.6.8')
    runner.run(suite)
