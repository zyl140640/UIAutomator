# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/5/31 17:05
@file: init.py
@desc: 该类主要用于开启和退出app
"""

from appium import webdriver

from common.adb_util import *


class AppStart:
    # 声明driver对象
    driver: webdriver = None

    # 使用classmethod方法，可以直接调用类中的属性和函数
    @classmethod
    def start(cls):
        caps = {
            "platformName": "Android",
            "deviceName": get_devices(),
            "platforVersion": get_devices_version(),
            "appPackage": "com.mimu.mshop",
            "appActivity": "com.mimu.mshop.ui.SplashActivity",
            "autoGrantPermissions": "true",
            "automationName": "UiAutomator2",
            "udid": "",
            'noReset': False,  # 不要重置App
        }

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(30)
        return cls.driver

    # 退出app
    @classmethod
    def quit(cls):
        cls.driver.quit()
