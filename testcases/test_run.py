# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/1 17:48
@file: run.py
@desc: 
"""
import time

from common.init import AppStart
from page.login_page import LoginPage
from page.shop_page import ShopPage


class TestRun:
    def setup(self):
        self.names = AppStart.start()

    def test_name(self):
        login = LoginPage(self.names)
        login.enter_iphone()
        time.sleep(3)
        shop = ShopPage(self.names)
        shop.shop_iphone()

    def teardown(self):
        AppStart.quit()
