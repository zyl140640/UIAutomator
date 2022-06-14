# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/14 13:28
@file: login_page.py
@desc: 我的-设置列表外层的的操作元素封装
"""
from common.base_page import BasePage


class MySettings(BasePage):

    def settings_button(self):
        self.click("id", "com.mimu.mshop:id/img_setting", "我的-账户与安全按钮")

    def lv_person_button(self):
        self.click("id", "com.mimu.mshop:id/lv_person", "设置列表-个人信息按钮")

    def lv_address_button(self):
        self.click("id", "com.mimu.mshop:id/lv_address", "设置列表-账户与安全")

    def lv_safety_button(self):
        self.click("id", "com.mimu.mshop:id/lv_safety", "设置列表-地址管理")

    def tv_withdraw_button(self):
        self.click("id", "com.mimu.mshop:id/tv_withdraw", "设置列表-支付/体现设置")

    def lv_bill_button(self):
        self.click("id", "com.mimu.mshop:id/lv_bill", "设置列表-发票抬头管理")

    def lv_about_button(self):
        self.click("id", "com.mimu.mshop:id/lv_about", "设置列表-关于迷姆")
