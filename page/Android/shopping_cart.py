# encoding: utf-8
"""
@author: 宋坤坤
@contact: cailyn.song@isysful.com
@time: 2022/6/22 17:43
@file: shopping_cart.py
@desc: 
"""
from common.base_page import BasePage


class ShoppingCart(BasePage):
    # 产品单选框
    radio_button = ("id", "test")

    # 定义底部导航栏方法
    def delete_goods(self):
        """
        点击底部导航栏首页
        """
        self.click(self.radio_button, '底部导航栏-首页')
