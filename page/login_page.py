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
    # 密码和手机号登录页面的-手机号码输入框
    phone_input_box = ("id", "com.mimu.mshop:id/et_ordinary_phone")
    # 登录页面-密码输入框
    password_input_box = ("id", "com.mimu.mshop:id/et_login_pwd")
    # 密码登录页面的登录按钮/手机号验证码登录页面的发送验证码
    login_button = ("id", "com.mimu.mshop:id/btn_reg_send")
    # 切换密码或者手机号登录页面按钮
    toggle_login_button = ("id", "com.mimu.mshop:id/menu_msg")
    # 登录页面忘记密码按钮
    login_forgot_password_button = ("id", "com.mimu.mshop:id/tv_login_forget")
    # 用户协议
    user_pact = ("id", "com.mimu.mshop:id/cb_register")
    # 其他登录方式 qq vx 支付宝
    login_qq = ("id", "com.mimu.mshop:id/img_qq")
    login_vx = ("id", "com.mimu.mshop:id/img_vx")
    login_zfb = ("id", "com.mimu.mshop:id/img_zfb")

    def input_account(self, account):
        """
        登录页面的手机号码输入框
        :param account: 手机号码
        """
        self.input_data(self.phone_input_box, "输入手机号码", account)

    def input_password(self, password):
        """
        登录页面的密码输入框
        :param password: 密码
        """
        self.input_data(self.password_input_box, "输入密码", password)

    def login(self):
        """
        密码登录页面的登录按钮/手机号验证码登录页面的发送验证码
        """
        self.click(self.login_button, "登录")

    def toggle_captcha_password_button(self):
        """
        切换至验证码登录或验证码登录的按钮
        """
        self.click(self.toggle_login_button, "切换到验证码登录页面")
        self.time.sleep(2)

    def forget_password_button(self):
        """
        密码登录页面的忘记密码按钮
        """
        self.click(self.forget_password_button(), "切换到验证码登录页面")

    def user_agreement_single_box(self):
        """
        手机号登录页面的用户协议按钮
        """
        self.click(self.user_pact, "点击用户勾选协议")

    def qq_login(self):
        """
        其他方式登录-QQ登录
        """
        self.click(self.login_qq, "QQ登录")

    def wechat_login(self):
        """
        其他方式登录-微信登录
        """
        self.click(self.login_vx, "微信登录")

    def zfb_login(self):
        """
        其他方式登录-支付宝登录
        """
        self.click(self.login_zfb, "支付宝登录")

    def login_password(self, account, password):
        """
        手机号+密码登录流程
        :param account: 手机号码
        :param password:密码
        """
        self.input_account(account)
        self.input_password(password)
        self.login()
