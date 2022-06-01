# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/5/31 17:07
@file: login_page.py
@desc: 
"""
# 欢迎页相关操作
from appium import webdriver
from selenium.webdriver.common.by import By
from page.account_login_page import AccountLoginPage
from page.base_page import BasePage


# 继承BasePage类
class LoginPage(BasePage):
    # 声明driver变量
    driver: webdriver = None
    # 隐私政策的同意按钮（根据xpath查找元素）
    _btn_agree = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView"
    # 账号密码登录按钮（根据id查找元素）
    _btn_account_pwd = (By.ID, "com.sina.weibo:id/tv_for_psw_login")

    # 进入账号密码登录页面
    def enter_account_login(self):
        # 调用xpath元素定位方法，点击隐私政策同意按钮
        self.find_xpath(self._btn_agree).click()
        # 调用id元素定位方法，进入账号密码登录页面
        self.find_element(self._btn_account_pwd).click()
        return AccountLoginPage(self.driver)
