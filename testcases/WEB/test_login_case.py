# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/16 16:08
@file: test_login_case.py
@desc:
"""
import logging

from common.selenium_init import WebStart
from page.WEB.login_page import LoginPasswordPage


class TestLogin:
    def setup_class(self):
        self.app = WebStart.start('edge')
        self.login = LoginPasswordPage(self.app)
        self.logger = logging

    def test_login(self):
        self.logger.info("------执行登录操作------")
        self.login.login_password_cookies()
        self.logger.info("------执行搜索操作------")
        self.login.query_api()

    @staticmethod
    def teardown_class():
        """
         类后置 执行退出操作
        """
        WebStart.quit()
