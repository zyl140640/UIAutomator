# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/1 17:45
@file: login_page.py
@desc: 
"""
import time
import logging
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class LoginPage(BasePage):

    def enter_iphone(self):
        self.assert_text((By.CLASS_NAME, "android.widget.EditText"), "输入手机号码", "输入您的手机号注册或登陆")
        self.input_data((By.ID, "com.mimu.mshop:id/et_ordinary_phone"), "输入手机号码", "15533065391")

        time.sleep(2)
        self.click((By.ID, "com.mimu.mshop:id/cb_register"), "勾选用户协议")
        time.sleep(5)
