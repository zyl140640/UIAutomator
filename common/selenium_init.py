# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/6 9:25
@file: selenium_init.py
@desc: 
"""


from selenium import webdriver
from threading import Thread
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service


class WebStart:
    driver: webdriver = None

    @classmethod
    def start(cls, web_browser, url):
        browser = web_browser.lower()
        # 判断browser的值
        if browser == "safari":
            cls.driver = webdriver.Safari()
        elif browser == "ie":
            cls.driver = webdriver.Ie()
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            service = Service(executable_path="./config/driver/geckodriver")
            cls.driver = webdriver.Firefox(options=options, service=service)
        else:
            cls.driver = webdriver.Chrome()
            options = webdriver.ChromeOptions()
            try:
                service = Service(executable_path="./config/driver/chromedriver.exe")
                cls.driver = webdriver.Chrome(options=options, service=service)
            except WebDriverException:
                service = Service(executable_path="./config/driver/chromedriver")
                cls.driver = webdriver.Chrome(options=options, service=service)
        # 打开目标网址
        cls.driver.get(url)
        return cls.driver

    @classmethod
    def quit(cls):
        cls.driver.quit()



    # @classmethod
    # def start(cls):
    #     options = webdriver.ChromeOptions()
    #     try:
    #         service = Service(executable_path="./config/driver/chromedriver.exe")
    #         cls.driver = webdriver.Chrome(options=options, service=service)
    #         #return cls.driver
    #     except WebDriverException:
    #         service = Service(executable_path="./config/driver/chromedriver")
    #         cls.driver = webdriver.Chrome(options=options, service=service)
    #         #return cls.driver

    # 退出app
