import unittest

import time


# 定义测试类  ---  必须继承unittest.TestCase
class TestFixture(unittest.TestCase):
    # 重写父类的setUp方法--方法级别Fixture -- 测试方法-执行前自动执行
    def setUp(self):
    # 重写父类的tearDown方法--方法级别Fixture -- 测试方法-执行后自动执行
    # 定义测试方法 --- 方法名必须是test开头
        print("打开浏览器...")
    def tearDown(self):
        # print("用例1_验证码不能为空验证")
        print("关闭浏览器...")

    # def test_02(self):
    #     print("打开浏览器...")
    def test_01(self):
        print("用例2_密码不能为空验证")
        print("关闭浏览器...")

