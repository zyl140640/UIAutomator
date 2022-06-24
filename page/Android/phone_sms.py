# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/2 9:34
@file: shop_page.py
@desc: 
"""
import time

from common.base_page import BasePage


class PhoneSmsPage(BasePage):

    def shop_iphone(self):
        self.driver.get("http://192.168.31.166:8090/#/goods/management")
        time.sleep(2)
