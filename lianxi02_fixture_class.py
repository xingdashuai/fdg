import unittest

import time


# 定义测试类  ---  必须继承unittest.TestCase
class TestFixture(unittest.TestCase):
    # 重写父类的setUpClass方法--类级别Fixture -- 测试类中所有测试方法-执行前自动执行
    @classmethod
    def setUpClass(cls):
        print("打开浏览器...")
    # 重写父类的tearDownClass方法--类级别Fixture -- 测试类中所有测试方法-执行后自动执行
    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器...")


    # 定义测试方法 --- 方法名必须是test开头
    def test_01(self):
        print("用例1_验证码不能为空验证")

    def test_02(self):

        print("用例2_密码不能为空验证")
