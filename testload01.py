import unittest

# 使用默认的加载对象加载用例 defaultTestLoader是默认的加载对象。
suite = unittest.defaultTestLoader.discover('case', 'case01.py')
unittest.TextTestRunner().run(suite)


# Fixture 测试夹具设计一种代码结构，在某些特定的情况下会自动执行
# 有方法级别的， 在每个测试方法执行前后都会调用的结构.方法级别的和类级别的，不需要同时出现，根据需要自行选择
def setUp(self):
    # 每个方法执行前都会执行
    pass


def tearDown(self):
    # 在每个测试方法执行后都执行
    pass


# 类级别的在每个测试类执行前后，都会调用的结构。在整个类执行前一次，后面一次。
# 类级别的Fixture方法，是一个类方法
# 在类所有的方法之前
@classmethod
def setUp():
    pass


@classmethod
def tearDown():
    pass


# 模块级别的。在每个代码文件执行前后需要执行的结构
def setUpModule():
    pass


def tearDownModule():
    pass
