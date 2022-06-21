# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/1 17:48
@file: run.py
@desc: 
"""

from common.appium_init import AppStart
from page.login_page import LoginPasswordPage
from page.main_page import MainPage


class TestLogin:
    def setup_class(self):
        self.app = AppStart.start()
        self.login = LoginPasswordPage(self.app)
        self.main_page = MainPage(self.app)

    def test_password_login(self):
        """
        测试密码登录业务流程
        """
        self.main_page.my_nav()
        self.login.toggle_captcha_password_button()
        self.login.login_password(15533065391, "abcd1234567890123456")
        self.main_page.enter_market_page()

    def teardown_class(self):
        """
         类后置 执行退出操作
        """
        AppStart.quit()
