# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/5/31 17:06
@file: base_page.py
@desc: 基础类，封装元素定位操作

"""
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    # 初始化，定义driver的类型为WebDriver
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 根据id定位
    def find_element(self, locator):
        try:
            # 单个元素定位，获取到的是单个元素的位置
            return self.driver.find_element(*locator)
        except:
            # 多个相同id元素定位，获取到的是一个列表，具体某个元素的位置可以使用列表查询
            return self.driver.find_elements(*locator)

    # 根据xpath定位
    def find_xpath(self, locator):
        try:
            # 单个元素定位，获取到的是单个元素的位置
            return self.driver.find_element_by_xpath(locator)
        except:
            # 多个相同xpath元素定位，获取到的是列表，具体某个元素的位置可以使用列表查询（xpath为唯一定位，一般不需要使用到该方法）
            return self.driver.find_elements(locator)

    # 根据class name定位
    def find_classname(self, *locator):
        # classname定位使用较少，一般用于无法使用id定位和xpath定位时使用，获取到的是列表，具体某个元素的位置可以使用列表查询
        return self.driver.find_elements_by_class_name(*locator)
