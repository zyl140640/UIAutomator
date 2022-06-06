# encoding: utf-8
"""
@author: 宋坤坤
@contact: cailyn.song@isysful.com
@time: 2022/6/6 17:18
@file: Navigation_Bar.py
@desc: 封装底部导航栏
"""
from common.base_page import BasePage


class Navigation_Bar(BasePage):

    def main(self):
        """
        点击底部导航栏首页
        """
        self.click('id', 'com.mimu.mshop:id/navigation_bar_item_large_label_view', '底部导航栏-首页')


    def category(self):
        """
        点击底部导航栏分类
        """
        self.click('xpath', '//android.widget.FrameLayout[@content-desc="分类"]/android.view.ViewGroup/android.widget.TextView', '底部导航栏-分类')

    def find(self):
        """
        点击底部导航栏发现
        """
        self.click('xpath', '//android.widget.FrameLayout[@content-desc="发现"]/android.view.ViewGroup/android.widget.TextView', '底部导航栏-发现')

    def cart(self):
        """
        点击底部导航栏购物车
        """
        self.click('id', '//android.widget.FrameLayout[@content-desc="购物车"]/android.view.ViewGroup/android.widget.TextView', '底部导航栏-购物车')

    def my(self):
        """
        点击底部导航栏我的
        """
        self.click('xpath', '//android.widget.FrameLayout[@content-desc="我的"]/android.view.ViewGroup/android.widget.TextView', '底部导航栏-我的')


