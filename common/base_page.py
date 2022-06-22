# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/5/31 17:06
@file: base_page.py
@desc: 基础类，封装元素定位操作
定位使用优先级:
Android：AndroidUIAutomator > className = id = AccessibilityId > xpath。
iOS：iOSNsPredicateString > className = AccessibilityId> xpath。
"""
import logging
import time

import allure
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        """
        初始化，定义driver的类型为WebDriver
        :param driver: web驱动器
        """
        self.driver = driver
        self.logger = logging
        self.time = time

    def find_element(self, locate, img_doc, timeout=10, frequency=0.5):
        """
        检测定位元素是否存在  定位单个元素
        :param locate: 元素定位方式+路径
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:  WebElement元素地址
        """
        try:
            el = None
            wait = WebDriverWait(self.driver, timeout, frequency)
            if locate[0] == 'id':
                el = wait.until(lambda diver: self.driver.find_element(By.ID, locate[1]), message='没找到该元素')
            elif locate[0] == 'xpath':
                el = wait.until(lambda diver: self.driver.find_element(By.XPATH, locate[1]), message='没找到该元素')
            elif locate[0] == 'name':
                el = wait.until(lambda diver: self.driver.find_element(By.NAME, locate[1]), message='没找到该元素')
            elif locate[0] == 'css_selector':
                el = wait.until(lambda diver: self.driver.find_element(By.CSS_SELECTOR, locate[1]),
                                message='没找到该元素')
            elif locate[0] == 'tag_name':
                el = wait.until(lambda diver: self.driver.find_element(By.TAG_NAME, locate[1]), message='没找到该元素')
            elif locate[0] == 'partial_link_text':
                el = wait.until(lambda diver: self.driver.find_element(By.PARTIAL_LINK_TEXT, locate[1]),
                                message='没找到该元素')
            elif locate[0] == 'link_text':
                el = wait.until(lambda diver: self.driver.find_element(By.LINK_TEXT, locate[1]), message='没找到该元素')
            elif locate[0] == 'class_name':
                el = wait.until(lambda diver: self.driver.find_element(By.CLASS_NAME, locate[1]), message='没找到该元素')
            elif locate[0] == 'predicate':
                el = wait.until(lambda diver: self.driver.find_element_by_ios_predicate(locate[1]), message='没找到该元素')
            elif locate[0] == 'accessibility_id':
                el = wait.until(lambda diver: self.driver.find_element_by_accessibility_id(locate[1]), message='没找到该元素')
            if el is not None:
                return el
            self.logger.info("<{}>,元素<{}>定位成功".format(img_doc, locate[1]))
        except Exception as e:
            self.logger.error("<{}>元素<{}>定位失败！".format(img_doc, locate[1]))
            raise e

    def find_elements(self, locate, img_doc, timeout=10, frequency=0.5):
        """
        检测定位元素是否存在 多个元素
        :param locate: 元素定位方式+路径
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:  WebElement元素地址 返回list类型
        """
        try:
            el = None
            wait = WebDriverWait(self.driver, timeout, frequency)
            if locate[0] == 'id':
                el = wait.until(lambda diver: self.driver.find_elements(By.ID, locate[1]), message='没找到该元素')
            elif locate[0] == 'xpath':
                el = wait.until(lambda diver: self.driver.find_elements(By.XPATH, locate[1]), message='没找到该元素')
            elif locate[0] == 'name':
                el = wait.until(lambda diver: self.driver.find_elements(By.NAME, locate[1]), message='没找到该元素')
            elif locate[0] == 'css_selector':
                el = wait.until(lambda diver: self.driver.find_elements(By.CSS_SELECTOR, locate[1]),
                                message='没找到该元素')
            elif locate[0] == 'tag_name':
                el = wait.until(lambda diver: self.driver.find_elements(By.TAG_NAME, locate[1]), message='没找到该元素')
            elif locate[0] == 'partial_link_text':
                el = wait.until(lambda diver: self.driver.find_elements(By.PARTIAL_LINK_TEXT, locate[1]),
                                message='没找到该元素')
            elif locate[0] == 'link_text':
                el = wait.until(lambda diver: self.driver.find_elements(By.LINK_TEXT, locate[1]), message='没找到该元素')
            elif locate[0] == 'class_name':
                el = wait.until(lambda diver: self.driver.find_elements(By.CLASS_NAME, locate[1]), message='没找到该元素')
            elif locate[0] == 'predicate':
                el = wait.until(lambda diver: self.driver.find_elements_by_ios_predicate(locate[1]), message='没找到该元素')
            elif locate[0] == 'accessibility_id':
                el = wait.until(lambda diver: self.driver.find_elements_by_accessibility_id(locate[1]), message='没找到该元素')
            if el is not None:
                return el
            self.logger.info("<{}>,元素<{}>定位成功".format(img_doc, locate[1]))
        except Exception as e:
            self.logger.error("<{}>元素<{}>定位失败！".format(img_doc, locate[1]))
            raise e

    def click(self, locate, img_doc):
        """
        点击按钮
        :param locate:  元素定位方式+路径  元组类型传入
        :param img_doc: 截图说明
        """
        try:
            if len(locate) == 2:
                el = self.find_element(locate, img_doc)
                el.click()
                self.logger.info("点击<{}>成功,元素和定位方式:{}".format(img_doc, locate))
            else:
                el = self.find_elements(locate, img_doc)
                el[locate[2]].click()
                self.logger.info("点击<{}>成功,元素和定位方式:{}".format(img_doc, locate))
        except Exception as e:
            self.logger.error("点击<{}>失败,元素和定位方式:{}".format(img_doc, locate))
            self.add_allure_attach(img_doc)
            raise e

    def input_data(self, locate, img_doc, text):
        """
        对输入框输入文本内容
        :param locate: 元素定位方式
        :param text: 输入的文本内容
        :param img_doc: 截图说明
       """
        try:
            if len(locate) == 2:
                el = self.find_element(locate, img_doc)
                self.logger.info("在<{}>功能的<{}>元素中输入内容为{}: ".format(img_doc, locate[1], text))
                el.send_keys(text)
            else:
                el = self.find_elements(locate, img_doc)
                self.logger.info("在<{}>功能的<{}>元素中输入内容为{}: ".format(img_doc, locate[1], text))
                el[locate[2]].send_keys(text)
        except Exception as e:
            self.logger.error("在元素<{}>中输入内容{}失败！".format(locate[1], text))
            self.add_allure_attach(img_doc)
            raise e

    def assert_text(self, locate, img_doc, expect_text):
        """
        获取WebElement对象的文本值
        :param locate: 元素定位方式
        :param expect_text: 预期文本
        :param img_doc: 截图说明
        :return: WebElement对象的文本值
        """
        try:
            self.logger.info("在{}中获取元素<{}>的文本值".format(img_doc, locate[1]))
            el = self.find_element(locate, img_doc)
            assert el.text == expect_text, "{}断言失败".format(img_doc)
            return el.text
        except Exception as e:
            self.logger.error("在{}中获取元素<{}>的文本值失败！".format(img_doc, locate[1]))
            self.add_allure_attach(img_doc)
            raise e

    def get_text_click(self, locate, img_doc, text=None):
        """
        获取WebElement对象的文本内容并进行点击操作  不填写text则返回 元素对象列表
        :param text: 对象的文本内容 默认可以不填写
        :param locate: 元素定位方式+路径
        :param img_doc: 截图说明
        :return: WebElement对象的属性值 list类型
        """
        try:
            el = self.find_elements(locate, img_doc)
            for lists in el:
                self.logger.info("元素列表返回的{}".format(lists.text))
                if lists.text == text:
                    lists.click()
            return el
        except Exception as e:
            self.logger.error("在{}中获取元素<{}>的属性的文本内容失败！".format(img_doc, locate))
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

    def scroll_to_element(self, locate, img_doc):
        """
        selenium通过JS滑动到指定元素
        :param locate: 元素定位方式+路径
        :param img_doc: 截图说明
        :return:  WebElement元素地址
        """
        try:
            el = self.find_element(locate, img_doc)
            self.driver.execute_script("arguments[0].scrollIntoView();", el)
            self.logger.info("<{}>,<{}>定位成功".format(img_doc, locate[1]))
            return el
        except Exception as e:
            self.logger.error("<{}>页面元素<{}>定位失败！异常内容: <{}>".format(img_doc, locate[1], e))
            raise e

    def target_click(self, x1, y1, img_doc):  # x1,y1为你编写脚本时适用设备的实际坐标
        x_1 = x1 / 375  # 计算坐标在横坐标上的比例，其中375为iphone6s的宽
        y_1 = y1 / 667  # 计算坐标在纵坐标667为iphone6s的高
        x = self.driver.get_window_size()['width']  # 获取设备的屏幕宽度
        y = self.driver.get_window_size()['height']  # 获取设备屏幕的高度
        print(x_1 * x, y_1 * y)  # 打印出点击的坐标点
        try:
            self.driver.tap([(x_1 * x, y_1 * y)], 500)  # 模拟单手点击操作
        except Exception as e:
            self.logger.error("在{}中获取元素<{}>的属性{}的值失败！,异常内容: <{}>".format(img_doc, x1, y1, e))
            self.add_allure_attach(img_doc)
            raise e
