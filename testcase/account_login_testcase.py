# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/5/31 17:08
@file: account_login_testcase.py
@desc: # 手机账号密码登录测试用例
"""
from common.init import AppStart


class TestAccountLogin:
    # 初始化
    def setup(self):
        self.accountloginpage = AppStart.start().enter_account_login()

    # 输入格式错误的账号
    def test_error_format_account(self):
        # 设置输入的账号和密码
        account = "123123231321313"
        pwd = "asdfgh"
        # 调用输入账号密码函数
        self.accountloginpage.input_account_pwd(account, pwd)
        # 使用断言判断实际结果与预期结果是否一致，左边为实际结果，右边为预期结果
        assert self.accountloginpage.get_bounced_context() == "手机格式有问题，若非中国大陆手机号码请点击国际手机登录"

    # 退出app
    def teardown(self):
        AppStart.quit()
