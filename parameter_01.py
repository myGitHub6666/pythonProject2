# 参数化在测试方法中使用变量；来代替具体的测试数据，然后使用传参的方式将测试数据传递给方法的变量，好处是相似的代码不需要多次书写
# 1 测试数据一般都放json文件中，使用代码读取json文件，提取我们想要的数据
# 我们想要的数据类型为[[],[]]或者[(),(),()]这种形式
# 安装unittest插件。pip是python中包或者插件的管理工具，使用这个工具下载安装插件
# 验证 pip list 找一个有没有一个叫parameterized的
# 1 导包，2定义测试类 3书写测试方法（用得到的测试数据用变量代替）4 组织测试数据并传递
import unittest
from parameterized import parameterized
from tools_01 import login

date = [('admin', '12w3456', ' 登录成功'), ('root', '123456', '登录失败'), ('admin', '123123', '登录失败')]


# 列表中有几个元祖就是几组数据
class TestLogin(unittest.TestCase):
    def test_login(self, username, password, expect):
        self.assertEqual(expect, login(username, password))


# 组织测试数据并传参
