import unittest
import time
from selenium import webdriver

# 定义测试类  ---  必须继承unittest.TestCase
class TestLogin(unittest.TestCase):
    # 重写父类的setUp方法--方法级别Fixture -- 测试方法-执行前自动执行
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://localhost")

    # 重写父类的tearDown方法--方法级别Fixture -- 测试方法-执行后自动执行


    # 定义测试方法 --- 方法名必须是test开头
    # 用例01 -- 验证码不能为空
    def test_login01_yzmwk(self):
        # 实例化浏览器驱动对象
        time.sleep(2)
        self.driver.quit()

        # 业务操作
        # a.首页点击登录--进入登录页
        self.driver.find_element_by_link_text("登录").click()
        # b.输入用户名,密码
        self.driver.find_element_by_id("username").send_keys("13012345678")
        self.driver.find_element_by_id("password").send_keys("123456")
        # c.点击登录按钮
        self.driver.find_element_by_css_selector("[name='sbtbutton']").click()
        # d.获取错误信息
        msg = self.driver.find_element_by_class_name("layui-layer-content").text
        print("msg:", msg)

        # 断言是否提示信息是否包含 "验证码不能为空"
        self.assertIn("验证码不能为空123123213123", msg)

        # 退出浏览器驱动对象
        time.sleep(2)
        self.driver.quit()

    # 用例02 -- 密码不能为空
    def test_login02_mawk(self):
        driver = self.driver
        # 实例化浏览器驱动对象
        # 业务操作
        # a.首页点击登录--进入登录页
        driver.find_element_by_link_text("登录").click()
        # b.输入用户名,验证码
        driver.find_element_by_id("username").send_keys("13012345678")
        driver.find_element_by_id("verify_code").send_keys("8888")
        # c.点击登录按钮
        driver.find_element_by_css_selector("[name='sbtbutton']").click()
        # d.获取错误信息
        msg = driver.find_element_by_class_name("layui-layer-content").text
        print("msg:", msg)

        # 断言是否提示信息是否包含 "密码不能为空"
        self.assertIn("密码不能为空", msg)

        # 退出浏览器驱动对象
        time.sleep(2)
        driver.quit()