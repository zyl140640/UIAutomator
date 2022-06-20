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

    def input_account(self, account):
        """
        登录页面的手机号码输入框
        :param account: 手机号码
        """
        self.input_data("id", "com.mimu.mshop:id/et_ordinary_phone", "输入手机号码", account)

    def input_password(self, password):
        """
        登录页面的密码输入框
        :param password: 密码
        """
        self.input_data("id", "com.mimu.mshop:id/et_login_pwd", "输入密码", password)

    def login_button(self):
        """
        密码登录页面的登录按钮/手机号验证码登录页面的发送验证码
        """
        self.click("id", "com.mimu.mshop:id/btn_reg_send", "登录")

    def toggle_captcha_password_button(self):
        """
        切换至验证码登录或验证码登录的按钮
        """
        self.click("id", "com.mimu.mshop:id/menu_msg", "切换到验证码登录页面")

    def forget_password_button(self):
        """
        密码登录页面的忘记密码按钮
        """
        self.click("id", "com.mimu.mshop:id/tv_login_forget", "切换到验证码登录页面")

    def user_agreement_single_box(self):
        """
        手机号登录页面的用户协议按钮
        """
        self.click("id", "com.mimu.mshop:id/cb_register", "点击用户勾选协议")

    def qq_login(self):
        """
        其他方式登录-QQ登录
        """
        self.click("id", "com.mimu.mshop:id/img_qq", "QQ登录")

    def wechat_login(self):
        """
        其他方式登录-微信登录
        """
        self.click("id", "com.mimu.mshop:id/img_wx", "微信登录")

    def zfb_login(self):
        """
        其他方式登录-支付宝登录
        """
        self.click("id", "com.mimu.mshop:id/img_zfb", "支付宝登录")

    def login_password(self, account, password):
        """
        手机号+密码登录流程
        :param account: 手机号码
        :param password:密码
        """
        self.input_account(account)
        self.input_password(password)
        self.login_button()
