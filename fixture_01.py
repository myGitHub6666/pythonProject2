import unittest


class TestLogin(unittest.TestCase):
    def setUp(self):
        print("每一个测试方法执行前都会调用的方法")

    def tearDown(self):
        print("每个测试方法之后都会调用的方法")

    @classmethod  # 类方法前面都要加上装饰器
    def setUpClass(cls):
        print("打开浏览器")

    def tearDownClass(cls):
        print("关闭浏览器")

    def test_1(self):
        print("请输入正确的用户名密码和验证码。点击登录")

    def test_2(self):
        print("请输入错误的用户名密码和验证码")
