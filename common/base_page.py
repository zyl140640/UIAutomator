# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/5/31 17:06
@file: base_page.py
@desc: 基础类，封装元素定位操作

"""
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    # 初始化，定义driver的类型为WebDriver
    def __init__(self, driver: WebDriver):
        """
        :param driver: web驱动器
        """
        self.driver = driver

    def find_element(self, locate_type, value):
        """
        定位单元素方法
        :param locate_type: 定位类型 如: id,name,xpath
        :param value: 元素地址
        :return: 返回元素内容
        """
        el = None
        try:
            if locate_type == 'id':
                el = self.driver.find_element(By.ID, value)
            elif locate_type == 'name':
                el = self.driver.find_element(By.NAME, value)
            elif locate_type == 'class':
                el = self.driver.find_element(By.CLASS_NAME, value)
            elif locate_type == 'xpath':
                el = self.driver.find_element(By.XPATH, value)
            elif locate_type == 'tag':
                el = self.driver.find_element(By.TAG_NAME, value)
            elif locate_type == 'css':
                el = self.driver.find_element(By.CSS_SELECTOR, value)
            elif locate_type == 'text':
                el = self.driver.find_element(By.LINK_TEXT, value)
            elif locate_type == 'partial':
                el = self.driver.find_element(By.PARTIAL_LINK_TEXT, value)
            elif locate_type == 'selector':
                el = self.driver.find_element(By.CSS_SELECTOR, value)
            if el is not None:
                return el
        except:
            logging.Logger.info("未获取到该元素")
            raise  # 抛出异常

    def find_elements(self, locate_type, value):
        """
        定位多元素方法[列表元素]list类型
        :param locate_type: 定位类型 如: id,name,xpath
        :param value: 元素地址
        :return: 返回一个list类型的元素  需要变量名+[]进行使用
        """
        el = None
        try:
            if locate_type == 'id':
                el = self.driver.find_elements(By.ID, value)
            elif locate_type == 'name':
                el = self.driver.find_elements(By.NAME, value)
            elif locate_type == 'class':
                el = self.driver.find_elements(By.CLASS_NAME, value)
            elif locate_type == 'xpath':
                el = self.driver.find_elements(By.XPATH, value)
            elif locate_type == 'tag':
                el = self.driver.find_elements(By.TAG_NAME, value)
            elif locate_type == 'css':
                el = self.driver.find_elements(By.CSS_SELECTOR, value)
            elif locate_type == 'text':
                el = self.driver.find_elements(By.LINK_TEXT, value)
            elif locate_type == 'partial':
                el = self.driver.find_elements(By.PARTIAL_LINK_TEXT, value)
            elif locate_type == 'selector':
                el = self.driver.find_elements(By.CSS_SELECTOR, value)
            if el is not None:
                return el
        except:
            logging.Logger.info("未获取到该元素")
            raise  # 抛出异常
