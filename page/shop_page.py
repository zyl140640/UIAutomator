# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/2 9:34
@file: shop_page.py
@desc: 
"""
import time

from selenium.webdriver.common.by import By

from common.base_page import BasePage


class ShopPage(BasePage):

    def shop_iphone(self):
        self.click((By.ID, "com.mimu.mshop:id/cb_register"), "取消勾选用户协议")
        time.sleep(2)
        self.input_data((By.ID, "com.mimu.mshop:id/et_ordinary_phone"), "输入手机号码", "15533065391")
        time.sleep(5)
