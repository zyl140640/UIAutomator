# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/5/31 17:06
@file: base_page.py
@desc: 基础类，封装元素定位操作

"""
import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        """
        初始化，定义driver的类型为WebDriver
        :param driver: web驱动器
        """
        self.driver = driver
        self.logger = logging

    def find_element(self, locate_type, value, img_doc, timeout=10, frequency=0.5):
        """
        检测定位元素是否存在
        :param locate_type: 元素定位方式
        :param value:  页面元素路径
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:  WebElement元素地址
        """
        try:
            el = None
            wait = WebDriverWait(self.driver, timeout, frequency)
            if locate_type == 'id':
                el = wait.until(lambda diver: self.driver.find_element(By.ID, value), message='没找到该元素')
            elif locate_type == 'xpath':
                el = wait.until(lambda diver: self.driver.find_element(By.XPATH, value), message='没找到该元素')
            elif locate_type == 'name':
                el = wait.until(lambda diver: self.driver.find_element(By.NAME, value), message='没找到该元素')
            elif locate_type == 'css_selector':
                el = wait.until(lambda diver: self.driver.find_element(By.CSS_SELECTOR, value), message='没找到该元素')
            elif locate_type == 'tag_name':
                el = wait.until(lambda diver: self.driver.find_element(By.TAG_NAME, value), message='没找到该元素')
            elif locate_type == 'partial_link_text':
                el = wait.until(lambda diver: self.driver.find_element(By.PARTIAL_LINK_TEXT, value), message='没找到该元素')
            elif locate_type == 'link_text':
                el = wait.until(lambda diver: self.driver.find_element(By.LINK_TEXT, value), message='没找到该元素')
            elif locate_type == 'class_name':
                el = wait.until(lambda diver: self.driver.find_element(By.CLASS_NAME, value), message='没找到该元素')
            if el is not None:
                return el
            self.logger.info("<{}>,<{}>定位成功".format(img_doc, value))
        except Exception as e:
            self.logger.error("<{}>页面元素<{}>定位失败！异常内容: <{}>".format(img_doc, value, e))
            raise e

    def click(self, locate_type, value, img_doc):
        """
        点击按钮
        :param value: 页面元素路径
        :param locate_type:  元素定位方式
        :param img_doc: 截图说明
        :return:
        """
        try:
            el = self.find_element(locate_type, value, img_doc)
            el.click()
            self.logger.info("在<{}>中,点击元素<{}>成功".format(img_doc, value))
        except Exception as e:
            self.logger.error("<{}>中,点击元素<{}>失败,异常内容: <{}>".format(img_doc, value, e))
            self.add_allure_attach(img_doc)
            raise e

    def input_data(self, locate_type, value, img_doc, text):
        """
        对输入框输入文本内容
        :param value: 页面元素路径
        :param locate_type: 元素定位方式
        :param text: 输入的文本内容
        :param img_doc: 截图说明
        :return:
       """
        try:
            el = self.find_element(locate_type, value, img_doc)
            self.logger.info("在<{}>功能的<{}>元素中输入内容为{}: ".format(img_doc, value, text))
            el.send_keys(text)
        except Exception as e:
            self.logger.error("在元素<{}>中输入内容{}失败！,异常内容: <{}>".format(locate_type, text, e))
            self.add_allure_attach(img_doc)
            raise e

    def assert_text(self, locate_type, value, img_doc, expect_text):
        """
        获取WebElement对象的文本值
        :param value: 页面元素路径
        :param locate_type: 元素定位方式
        :param expect_text: 预期文本
        :param img_doc: 截图说明
        :return: WebElement对象的文本值
        """
        try:
            self.logger.info("在{}中获取元素<{}>的文本值".format(img_doc, locate_type))
            el = self.find_element(locate_type, value, img_doc)
            assert el.text == expect_text, "{}断言失败".format(img_doc)
            return el.text
        except Exception as e:
            self.logger.error("在{}中获取元素<{}>的文本值失败！,异常内容: <{}>".format(img_doc, locate_type, e))
            self.add_allure_attach(img_doc)
            raise e

    def get_attribute(self, locate_type, value, img_doc, attr_name):
        """
        获取WebElement对象的属性值
        :param value: 页面元素路径
        :param locate_type: 元素定位方式
        :param img_doc: 截图说明
        :param attr_name: 属性名称
        :return: WebElement对象的属性值
        """
        try:
            el = self.find_element(locate_type, value, img_doc)
            self.logger.info("成功获取<{}>元素<{}>属性{}的值".format(img_doc, attr_name, value))
            return el.get_attribute(attr_name)
        except Exception as e:
            self.logger.error("在{}中获取元素<{}>的属性{}的值失败！,异常内容: <{}>".format(img_doc, attr_name, value, e))
            self.add_allure_attach(img_doc)
            raise e

    def get_size(self):
        """
        获取界面大小
        :return: 返回界面大小
        """
        size = self.driver.get_window_size()
        self.logger.info("屏幕宽度: {},屏幕高度: {}".format(size['width'], size['height']))
        return size

    def add_allure_attach(self, img_doc):
        """
        allure 报告中添加失败截图附件
        :param img_doc: 截图说明
        """
        with allure.step("添加失败截图"):
            file = self.driver.get_screenshot_as_png()
            allure.attach(file, img_doc, allure.attachment_type.PNG)
