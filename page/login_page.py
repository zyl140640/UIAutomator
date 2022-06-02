# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/1 17:45
@file: login_page.py
@desc: 
"""
import time

from common.base_page import BasePage


class LoginPage(BasePage):

    def enter_iphone(self):
        self.find_element('id', "com.mimu.mshop:id/et_ordinary_phone").send_keys("15533065391")
        time.sleep(2)
        self.find_element('id', "com.mimu.mshop:id/cb_register").click()
        time.sleep(5)
