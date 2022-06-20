# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/16 16:08
@file: web.py
@desc: 
"""
import time

from common.base_page import BasePage
from common.selenium_init import WebStart


class Login(BasePage):

    def login(self):
        self.driver.get("http://192.168.31.166:8090/#/user/login")
        time.sleep(4)


if __name__ == '__main__':
    app = WebStart.start()
    login = Login(app)
    login.login()
