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
from common.yaml_util import read_yaml_key


class LoginPage(BasePage):

    def enter_iphone(self):
        el = read_yaml_key('data/page_element_v1.0/login_page.yaml', 'phone_number_input_box')
        self.assert_text(el['locate_type'], el['path'], el['img_doc'], "输入您的手机号注册或登陆l")
        self.input_data(el['locate_type'], el['path'], el['img_doc'], "15533065391")
        #
        # time.sleep(2)
        # self.click((By.ID, "com.mimu.mshop:id/cb_register"), "勾选用户协议")
        time.sleep(5)
