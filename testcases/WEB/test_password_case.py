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


class TestPassword:
    def setup_class(self):
        self.app = WebStart.start('edge')
        self.login = LoginPasswordPage(self.app)
        self.logger = logging

    def test_password(self):
        self.logger.info("------执行使用cookie方式进行登录------")
        self.login.login_password_cookies()
        self.logger.info("------登录成功,进入添加区域操作------")
        self.login.add_quyu()
        self.logger.info("------添加区域成功,完成任务------")

    @staticmethod
    def teardown_class():
        """
         类后置 执行退出操作
        """
        WebStart.quit()
