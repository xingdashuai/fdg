# 在一个测试类中定义多个测试方法，查看每个测试方法执行完所花费的时
import time
from selenium import webdriver
import unittest

# 定义测试类  ---  必须继承unittest.TestCase
class TestLogin(unittest.TestCase):

    # 定义测试方法 --- 方法名必须是test开头
    # 用例01 -- 验证码不能为空
    def test_login01_yzmwk(self):

        # 实例化浏览器驱动对象
        driver =  webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("http://127.0.0.1/")
        # 业务操作
        # a.首页点击登录--进入登录页
        driver.find_element_by_link_text("登录").click()
        driver.find_element_by_id("username").send_keys("130123456")
        driver.find_element_by_id("password").send_keys("123456")
        # b.输入用户名,密码
        # c.点击登录按钮
        driver.find_element_by_class_name("J-login-submit").click()
        # d.获取错误信息
        msg = driver.find_element_by_class_name("layui-layer-content").text
        print(msg)
        # 断言是否提示信息是否包含 "验证码不能为空"
        self.assertIn("验证码不能为空",msg)

        # 退出浏览器驱动对象
        time.sleep(2)
        driver.quit()

    # 用例02 -- 密码不能为空
