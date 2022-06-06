# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/6 9:25
@file: selenium_init.py
@desc: 
"""

from selenium import webdriver


class WebStart:
    driver: webdriver = None

    @classmethod
    def start(cls):
        options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome(options=options)
        return cls.driver

    #
    # 退出app
    @classmethod
    def quit(cls):
        cls.driver.quit()