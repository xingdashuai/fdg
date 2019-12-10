import unittest

from nose_parameterized import parameterized


def myadd(a, b):
    return a + b
adta = [(1, 1, 2), (1, 0, 2), (0, 0, 0)]
def get_adta():
    return [(1, 1, 2), (1, 0, 2), (0, 0, 0)]

# 定义测试类  ---  必须继承unittest.TestCase
class TestMyadd(unittest.TestCase):
    # 定义测试方法 --- 方法名必须是test开头
    def test_myadd1(self):
        # 1,1  预期  2
        # result = myadd(1, 1)
        # print("result: ", result)
        # self.assertEqual(2, result)

    def test_myadd2(self):
        # 1,0  预期  1
    #     result = myadd(1, 0)
    #     print("result: ", result)
    #     self.assertEqual(1, result)
    # parameterized
    # def test_myadd3(self):
    #     # 0,0  预期  0
    #     result = myadd(0, 0)
    #     print("result: ", result)
    #     self.assertEqual(0, result)



    # 第一种 -- 直接数据写入参数化方法
    @parameterized.expand([(1,1,2),(1,0,2),(0,0,0)])
    def test_myadd5(self,x,y,h):
        result = myadd(x,y)
        print("resilt:",result)
        self.assertEqual(h,result)
    # 第二种 -- 通过变量保存测试数据
    @parameterized.expand(adta)
    def test_myadd6(self,x,y,h):
        result = myadd(x,y)
        print("result:",result)
        self.assertEqual(h,result)
    # 第三种 -- 通过方法返回测试数据--定义返回数据的方法
    @parameterized.expand(adta)
    def test_myadd7(self,x,y,h):
        # 0,0  预期  0
        result = myadd(x, y)
        print("result: ", result)
        self.assertEqual(h, result)
