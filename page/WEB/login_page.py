# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/1 17:45
@file: login_page.py
@desc: 密码登录页面的操作元素封装
"""
import time

import allure

from common.base_page import BasePage


class LoginPasswordPage(BasePage):
    def login_password(self, account, password):
        """
        手机号+密码登录流程
        :param account: 手机号码
        :param password:密码
        """
        self.driver.get("http://jxair.minhopeonline.com/login?redirect=%2Fdata%2FmultiSmultiP")
        self.input_clear(("class_name", "el-input__inner", 0), "输入账号")
        self.input_data(("class_name", "el-input__inner", 0), "输入账号", account)
        self.input_clear(("class_name", "el-input__inner", 1), "输入密码")
        self.input_data(("class_name", "el-input__inner", 1), "输入密码", password)
        self.input_data(("class_name", "el-input__inner", 2), "输入验证码", input('请输入验证码: '))
        self.click(("xpath", '//*[@id="app"]/div/form/div[4]/div/button'), "登录按钮")

    def query_api(self):
        time.sleep(4)
        self.click(("class_name", 'hamburger'), "展开侧边栏")
        time.sleep(4)
        self.click(("class_name", 'el-menu-item', 5), "AQI查询")
        time.sleep(3)
        self.click(("class_name", "el-button.el-button--primary.el-button--mini", 0), "搜索")

    @allure.step("添加区域信息")
    def add_quyu(self):
        time.sleep(3)
        self.click(("css_selector", '.hamburger'), "展开侧边栏")
        self.click(("css_selector", 'div:nth-child(5) .el-submenu__title'), "基础信息")
        time.sleep(3)
        self.click(("xpath", '//div[5]/li/ul/div/a/li/span'), "区域管理")
        time.sleep(3)
        self.click(("css_selector", ".is-plain > span"), "新增")
        self.input_data(("css_selector", ".is-required .el-input__inner"), "区域名称", 'python')
        self.click(("css_selector", ".el-button--medium:nth-child(1) > span"), "提交")

    @allure.step("登录空气质量监测平台")
    def login_password_cookies(self):
        self.driver.get("http://jxair.minhopeonline.com/login?redirect=%2Fdata%2FmultiSmultiP")
        # 程序打开网页后20秒内 “手动登陆账户”
        # 首先清除由于浏览器打开已有的cookies
        self.add_cookies()
