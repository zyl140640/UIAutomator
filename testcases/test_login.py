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
from page.navigation_bar import NavigationBarPage


class TestLogin:
    def setup_class(self):
        self.app = AppStart.start()
        self.login = LoginPasswordPage(self.app)
        self.nav = NavigationBarPage(self.app)

    def test_password_login(self):
        """
        测试密码登录业务流程
        """
        self.nav.my()
        self.login.toggle_captcha_password_button()
        self.login.login_password(15533065391, "abcd1234567890123456")

    def teardown_class(self):
        """
         类后置 执行退出操作
        """
        AppStart.quit()
