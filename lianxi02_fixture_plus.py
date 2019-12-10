import unittest

import time


# 定义setUpModule方法--模块级别Fixture -- 模块中所有测试方法-执行前自动执行
def setUpModule():
    print("模块级别setUpModule")
# 定义tearDownModule方法--模块级别Fixture -- 模块中所有测试方法-执行后自动执行
def tearDownModule():
    print("模块级别tearDownModule")
# 定义测试类  ---  必须继承unittest.TestCase
class TestFixture0(unittest.TestCase):
    # 重写父类的setUpClass方法--类级别Fixture -- 测试类中所有测试方法-执行前自动执行
    @classmethod
    def setUpClass(cls):
        print("类级别setUpClass")
    # 重写父类的tearDownClass方法--类级别Fixture -- 测试类中所有测试方法-执行后自动执行
    @classmethod
    def tearDownClass(cls):
        print("类级别tearDownClass")
    # 重写父类的setUp方法--方法级别Fixture -- 测试方法-执行前自动执行
    def setUp(self):
        print("方法级别setUp")
    # 重写父类的tearDown方法--方法级别Fixture -- 测试方法-执行后自动执行
    def tearDown(self):
        print("方法级别tearDown")
    # 定义测试方法 --- 方法名必须是test开头
    def test_01(self):
        print("用例1_验证码不能为空验证")

    def test_02(self):
        print("用例2_密码不能为空验证")
