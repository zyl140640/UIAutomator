# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/1 17:45
@file: login_page.py
@desc: 密码登录页面的操作元素封装
"""

from common.base_page import BasePage


class LoginPasswordPage(BasePage):

    def input_login_password(self, account, password):
        """
        密码登录页面的手机号+密码输入框
        :param account: 手机号码
        :param password: 密码
        """
        self.input_data("id", "com.mimu.mshop:id/et_ordinary_phone", "输入手机号码", account)
        self.input_data("id", "com.mimu.mshop:id/et_login_pwd", "输入密码", password)

    def login_password_button(self):
        """
        密码登录页面的登录按钮
        """
        self.click("id", "com.mimu.mshop:id/btn_reg_send", "登录")

    def shift_captcha(self):
        """
        密码登录页面的切换至验证码登录按钮
        """
        self.click("id", "com.mimu.mshop:id/menu_msg", "切换到验证码登录页面")

    def forget_password(self):
        """
        密码登录页面的忘记密码按钮
        """
        self.click("id", "com.mimu.mshop:id/menu_msg", "切换到验证码登录页面")

    def login_password(self, account, password):
        """
        手机号+密码登录流程
        :param account: 手机号码
        :param password:密码
        """
        self.input_login_password(account, password)
        self.login_password_button()
