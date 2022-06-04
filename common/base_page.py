# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/5/31 17:06
@file: base_page.py
@desc: 基础类，封装元素定位操作

"""
import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 初始化，定义driver的类型为WebDriver
    def __init__(self, driver: WebDriver):
        """
        :param driver: web驱动器
        """
        self.driver = driver
        self.logger = logging

    def find_element(self, locator, img_doc, timeout=10, frequency=0.5):
        """
        检测定位元素是否存在
        :param locator: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:  WebElement元素地址
        """
        try:
            self.logger.info("开始等待页面元素<{}>是否存在！".format(locator))
            el = WebDriverWait(self.driver, timeout, frequency).until(EC.presence_of_element_located(locator))
            return el
        except Exception as e:
            self.logger.error("页面元素<{}>等待可见失败！".format(locator))
            self.driver.save_screenshot("screenshots/{}.png".format(img_doc))
            raise e  # 抛出异常

    def click(self, locator, img_doc):
        """
        点击按钮
        :param locator: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :return:
        """
        try:
            self.logger.info("在{}中点击元素<{}>".format(img_doc, locator))
            el = self.find_element(locator, img_doc)
            el.click()
        except Exception as e:
            self.logger.error("在{}中点击元素<{}>失败！".format(img_doc, locator))
            self.driver.save_screenshot("screenshots/{}.png".format(img_doc))
            raise e  # 抛出异常

    def input_data(self, locator, img_doc, text):
        """
        对输入框输入文本内容
        :param text: 输入的文本内容
        :param locator: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :return:
       """
        try:
            self.logger.info("在{}中输入元素<{}>的内容为{}: ".format(img_doc, locator, text))
            el = self.find_element(locator, img_doc)
            el.send_keys(text)
        except Exception as e:
            self.logger.error("在元素<{}>中输入内容{}失败！".format(locator, text))
            self.driver.save_screenshot("screenshots/{}.png".format(img_doc))
            raise e  # 抛出异常

    def assert_text(self, locator, img_doc, expect_text):
        """
        获取WebElement对象的文本值
        :param expect_text: 预期文本
        :param locator: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :return: WebElement对象的文本值
        """
        try:
            self.logger.info("在{}中获取元素<{}>的文本值".format(img_doc, locator))
            el = self.find_element(locator, img_doc)
            assert el.text == expect_text
            return el.text
        except Exception as e:
            self.logger.error("在{}中获取元素<{}>的文本值失败！".format(img_doc, locator))
            self.driver.save_screenshot("screenshots/{}.png".format(img_doc))
            raise e  # 抛出异常

    def get_attribute(self, locator, img_doc, attr_name):
        """
        获取WebElement对象的属性值
        :param locator: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param attr_name: 属性名称
        :return: WebElement对象的属性值
        """
        try:
            self.logger.info("在{}中获取元素<{}>的属性{}的值".format(img_doc, locator, attr_name))
            el = self.find_element(locator, img_doc)
            return el.get_attribute(attr_name)
        except Exception as e:
            self.logger.error("在{}中获取元素<{}>的属性{}的值失败！".format(img_doc, locator, attr_name))
            self.driver.save_screenshot("screenshots/{}.png".format(img_doc))
            raise e  # 抛出异常
