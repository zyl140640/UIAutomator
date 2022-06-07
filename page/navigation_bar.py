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

    def main(self):
        """
        点击底部导航栏首页
        """
        self.click('id', 'com.mimu.mshop:id/homeFragment', '底部导航栏-首页')

    def category(self):
        """
        点击底部导航栏分类
        """
        self.click('id', 'com.mimu.mshop:id/sortFragment', '底部导航栏-分类')

    def find(self):
        """
        点击底部导航栏发现
        """
        self.click('id', 'com.mimu.mshop:id/findFragment', '底部导航栏-发现')

    def cart(self):
        """
        点击底部导航栏购物车
        """
        self.click('id', 'com.mimu.mshop:id/shopFragment', '底部导航栏-购物车')

    def my(self):
        """
        点击底部导航栏我的
        """
        self.click('id', 'com.mimu.mshop:id/mineFragment', '底部导航栏-我的')


