# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/5/31 17:08
@file: account_login_page.py
@desc: # 账号密码登录页面相关操作
"""
import time

from selenium.webdriver.common.by import By

from page.base_page import BasePage


# 继承BasePage类
class AccountLoginPage(BasePage):
    # 账号输入框
    _et_account = (By.ID, "com.sina.weibo:id/et_pws_username")
    # 密码输入框
    _et_pwd = (By.ID, "com.sina.weibo:id/et_pwd")
    # 登录按钮
    _btn_login = (By.ID, "com.sina.weibo:id/bn_pws_Login")
    # 手机号格式错误弹框的内容(底标为0),取消按钮(底标为2),弹框立即注册按钮或国际手机号登录按钮(底标为4)
    _tv_bounced_context = "android.widget.TextView"

    # 输入账号函数
    def input_account(self, account):
        # 清空账号输入框内容
        self.find_element(self._et_account).clear()
        # 账号输入框输入内容
        self.find_element(self._et_account).send_keys(account)

    # 输入密码函数
    def input_pwd(self, pwd):
        # 清空密码输入框内容
        self.find_element(self._et_pwd).clear()
        # 密码输入框输入内容
        self.find_element(self._et_pwd).send_keys(pwd)

    # 输入账号和密码函数
    def input_account_pwd(self, account, pwd):
        # 调用输入账号函数
        self.input_account(account)
        # 调用输入密码函数
        self.input_pwd(pwd)
        # 点击登录密码
        self.find_element(self._btn_login).click()

    # 输入错误格式的手机号码获取弹框内容函数
    def get_bounced_context(self):
        # 根据classname定位，将相同的classname元素存放在列表中
        bounced = self.find_classname(self._tv_bounced_context)
        # 手机号码格式错误弹框内容再列表的第一位，列表的下表从0开始，并将弹框的内容定义为text属性
        bounced_context = bounced[0].text
        time.sleep(1)
        # 输入账号密码后点击注册按钮，该按钮的位置在列表的第三位，故下标为2
        bounced[2].click()
        # 将获取到的弹框内容返回，以便后续调用函数时能获取到弹框内容
        return bounced_context
