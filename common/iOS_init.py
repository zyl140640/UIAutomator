# encoding: utf-8
"""
@author: 宋坤坤
@contact: cailyn.song@isysful.com
@time: 2022/7/14 09:49
@file: iOS_init.py
@desc: 
"""
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
    caps = {
        "platformName": "iOS",
        "appium:deviceName": "青岛迷姆的iPhone",
        "appium:platforVersion": "15.4.1",
        "appium:udid": "00008110-0016319E2E52801E",
        "appium:automationName": "XCUITest",
        "appium:app": "com.memevip.mshopping"
    }

    # 使用classmethod方法，可以直接调用类中的属性和函数
    @classmethod
    def start(cls):
        # caps = {
        #     "platformName": "Android",
        #     "deviceName": get_devices(),
        #     "platforVersion": get_devices_version(),
        #     "appPackage": "com.mimu.mshop",
        #     "appActivity": "com.mimu.mshop.ui.SplashActivity",
        #     "autoGrantPermissions": "true",
        #     "automationName": "UiAutomator2",
        #     "udid": "",
        #     'noReset': False,  # 不要重置App
        # }

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", cls.caps)
        cls.driver.implicitly_wait(30)
        return cls.driver

    # 退出app
    @classmethod
    def quit(cls):
        cls.driver.quit()
