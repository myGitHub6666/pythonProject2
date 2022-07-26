# testload(测试加载）和testsuite的作用是一样的，对功能的补充。用来组装测试用例的
# 在一个项目中Testcase的代码，一般放在一个单独的目录（case）
"""" TestLoader的使用"""
import unittest
# 实例化加载对象并添加用例
# unittest.TestLoader().discover('用例所在路径', "用例的代码文件名")
# 用例所在的路径建议使用相对路径。用例的代码文件名可以使用*（任意多个字符的通配符）
suite = unittest.TestLoader().discover("./case", 'case01.py') # ./case 表示当前目录的下级文件夹目录
unittest.TextTestRunner().run(suite)




