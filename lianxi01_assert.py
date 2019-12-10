import unittest


def myadd(a, b):
    return a + b


# 定义测试类  ---  必须继承unittest.TestCase
class TestMyadd(unittest.TestCase):
    # 定义测试方法 --- 方法名必须是test开头
    def test_myadd1(self):
        # 1,3  预期  4
        result = myadd(1, 3)
        print("检查实际是否符合预期:",result)
        # 断言是否相等
        # self.assertEqual(4,result)

        # 断言是否为真
        self.assertEqualTrue(False)

        # 断言是否包含
        # self.assertIn("hello","helworld")
        #     self.assertIsNone(None)