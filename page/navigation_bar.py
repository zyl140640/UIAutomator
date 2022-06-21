# encoding: utf-8
"""
@author: 宋坤坤
@contact: cailyn.song@isysful.com
@time: 2022/6/6 17:18
@file: Navigation_Bar.py
@desc: 封装底部导航栏
"""
from common.base_page import BasePage


class NavigationBarPage(BasePage):
    """
    nav_main: 底部导航栏-首页
    nav_category: 底部导航栏-分类
    nav_find: 底部导航栏-发现
    nav_cart: 底部导航栏-购物车
    nav_my: 底部导航栏-我的
    """
    nav_main = ('id', 'com.mimu.mshop:id/homeFragment')
    nav_category = ('id', 'com.mimu.mshop:id/sortFragment')
    nav_find = ('id', 'com.mimu.mshop:id/findFragment')
    nav_cart = ('id', 'com.mimu.mshop:id/shopFragment')
    nav_my = ('id', 'com.mimu.mshop:id/mineFragment')

    def main(self):
        """
        点击底部导航栏首页
        """
        self.click(self.nav_main, '底部导航栏-首页')

    def category(self):
        """
        点击底部导航栏分类
        """
        self.click(self.nav_category, '底部导航栏-分类')

    def find(self):
        """
        点击底部导航栏发现
        """
        self.click(self.nav_find, '底部导航栏-发现')

    def cart(self):
        """
        点击底部导航栏购物车
        """
        self.click(self.nav_cart, '底部导航栏-购物车')

    def my(self):
        """
        点击底部导航栏我的
        """
        self.click(self.nav_my, '底部导航栏-我的')
