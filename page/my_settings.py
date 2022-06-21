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
    # 我的右上角设置按钮
    setting_button = ("id", "com.mimu.mshop:id/img_setting")
    # 个人信息按钮
    user_info_button = ("id", "com.mimu.mshop:id/lv_person")
    # 设置列表-账户与安全
    account_security_button = ("id", "com.mimu.mshop:id/lv_address")
    # 地址管理
    address_management_button = ("id", "com.mimu.mshop:id/lv_safety")
    # 支付/体现设置
    pay_button = ("id", "com.mimu.mshop:id/tv_withdraw")
    # 发票管理
    invoice_management_button = ("id", "com.mimu.mshop:id/lv_bill")
    # 关于我们
    about_button = ("id", "com.mimu.mshop:id/lv_about")

    def settings_button(self):
        self.click(self.setting_button, "我的-账户与安全按钮")

    def lv_person_button(self):
        self.click(self.user_info_button, "设置列表-个人信息按钮")

    def lv_address_button(self):
        self.click(self.account_security_button, "设置列表-账户与安全")

    def lv_safety_button(self):
        self.click(self.address_management_button, "设置列表-地址管理")

    def tv_withdraw_button(self):
        self.click(self.pay_button, "设置列表-支付/体现设置")

    def lv_bill_button(self):
        self.click(self.invoice_management_button, "设置列表-发票抬头管理")

    def lv_about_button(self):
        self.click(self.about_button, "设置列表-关于迷姆")
