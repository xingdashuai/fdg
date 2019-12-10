import unittest

# 定义测试类  ---  必须继承unittest.TestCase
import time
from selenium import webdriver


class TestLogin(unittest.TestCase):

    # 定义测试方法 --- 方法名必须是test开头
    # 用例01 -- 验证码不能为空
    def test_login01_yzmwk(self):
        # 实例化浏览器驱动对象
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("http://localhost")

        # 业务操作
        # a.首页点击登录--进入登录页
        driver.find_element_by_link_text("登录").click()
        # b.输入用户名,密码
        driver.find_element_by_id("username").send_keys("13012345678")
        driver.find_element_by_id("password").send_keys("123456")
        # c.点击登录按钮
        driver.find_element_by_css_selector("[name='sbtbutton']").click()
        # d.获取错误信息
        msg = driver.find_element_by_class_name("layui-layer-content").text
        print("msg:", msg)

        # 断言是否提示信息是否包含 "验证码不能为空"
        # 断言失败后保存截图,继续抛出异常  try - except
        try:
            self.assertIn("验证码不能为空fff", msg)
        except Exception as e:
            driver.get_screenshot_as_file("./a.png")
            raise e




        # 退出浏览器驱动对象
        time.sleep(2)
        driver.quit()

    # 用例02 -- 密码不能为空
    # def test_login02_mawk(self):
    #     pass