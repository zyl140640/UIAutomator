# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/1 17:48
@file: run.py
@desc: 
"""
import logging
import time

from selenium.webdriver.common.by import By

from common.appium_init import AppStart
from page.Android.login_page import LoginPasswordPage
from page.Android.main_page import MainPage
from common.base_page import BasePage


class TestLogin:
    def setup(self):
        self.app = AppStart.start()
        self.base = BasePage(self.app)
        self.login = LoginPasswordPage(self.app)
        self.main_page = MainPage(self.app)


    def test_password_login(self):
        """
        测试密码登录业务流程
        """

        time.sleep(3)
        text_list = self.base.get_elements_text(self.main_page.vajra_market_icon, "金刚区")
        exp_text = ['超市', '餐厅', '门店', '优惠券', '会员']
        assert exp_text == text_list, logging.info("文字错误")
        print(text_list)
        self.main_page.my_nav()
        self.login.toggle_captcha_password_button()
        self.login.login_password(15533065391, "abcd1234567890123456")


        # self.main_page.enter_vip_page()
        time.sleep(3)

    def teardown(self):
        """
         类后置 执行退出操作
        """
        AppStart.quit()
