import unittest
# 定义测试类  ---  必须继承unittest.TestCase
class TestFixture(unittest.TestCase):

    # 定义测试方法 --- 方法名必须是test开头
    def test_01(self):
        print("打开浏览器...")
        print("用例1_验证码不能为空验证")
        print("关闭浏览器...")


    def test_02(self):
        print("打开浏览器...")
        print("用例2_密码不能为空验证")
        print("关闭浏览器...")