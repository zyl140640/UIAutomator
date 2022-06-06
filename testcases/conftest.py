# encoding: utf-8
"""
@author: 宋坤坤
@contact: cailyn.song@isysful.com
@time: 2022/6/6 09:55
@file: conftest.py
@desc: 
"""
import os

import allure
import pytest

from common.init import AppStart


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     '''
#     获取每个用例状态的钩子函数
#     :param item:
#     :param call:
#     :return:
#     '''
#     # 获取钩子方法的调用结果
#     outcome = yield
#     _driver = AppStart.start()
#     rep = outcome.get_result()
#     # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             # let's also access a fixture for the fun of it
#             if "tmpdir" in item.fixturenames:
#                 extra = " (%s)" % item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#             f.write(rep.nodeid + extra + "\n")
#         # 添加allure报告截图
#         if hasattr(_driver, "get_screenshot_as_png"):
#
#             with allure.step('添加失败截图...'):
#                 allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


