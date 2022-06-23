# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/14 15:13
@file: test.py
@desc:
"""
import time

from common.base_page import BasePage
from common.selenium_init import WebStart


class TestWeb:
    el = ("xpath", '/html/body/article[1]/div[5]/p[1]')

    def setup_class(self):
        self.driver = WebStart.start("chrome", "http://192.168.31.166:8090/")
        self.web = WebStart
        self.base = BasePage(self.driver)

    def test_open_web(self):
        """
        测试密码登录业务流程
        """
        time.sleep(1)
        self.driver.maximize_window()
        self.base.input_data(('xpath','//*[@id="username"]') , "用户名",'123')
        time.sleep(2)
        self.base.input_data(('xpath', '//*[@id="password"]'), "密码",'123')
        time.sleep(1)
        self.base.click(('xpath', '//*[@id="root"]/div/div/div[2]/form/button[2]/span'), "确认")

        # self.driver.execute_script("scrollTo(100, 2000);")

        time.sleep(2)


    def teardown_class(self):
        """
         类后置 执行退出操作
        """

        WebStart.quit()
