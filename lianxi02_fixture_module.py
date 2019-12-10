import unittest

import time


# 定义setUpModule方法--模块级别Fixture -- 模块中所有测试方法-执行前自动执行
def setUpModule():
    print("打开浏览器。。。")
def tearDownModule():
    print("关闭浏览器。。。")
# 定义tearDownModule方法--模块级别Fixture -- 模块中所有测试方法-执行后自动执行
# 定义测试类  ---  必须继承unittest.TestCase
class TestFixture0(unittest.TestCase):

    # 定义测试方法 --- 方法名必须是test开头
    def test_01(self):
        print("用例1_验证码不能为空验证")

    def test_02(self):
        print("用例2_密码不能为空验证")


class TestFixture1(unittest.TestCase):

    # 定义测试方法 --- 方法名必须是test开头
    def test_01(self):
        print("用例1_验证码不能为空验证")

    def test_02(self):
        print("用例2_密码不能为空验证")
