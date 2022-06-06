# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/1 17:48
@file: run.py
@desc: 
"""

from common.appium_init import AppStart
from page.login_password import LoginPasswordPage


class TestRun:
    def setup_class(self):
        self.app = AppStart.start()
        self.login = LoginPasswordPage(self.app)

    def test_name(self):
        self.login.login_password(15533065391, 123456)

    def teardown_class(self):
        """
         类后置 执行退出操作
        """
        AppStart.quit()
