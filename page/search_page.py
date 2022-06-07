# encoding: utf-8
"""
@author: 宋坤坤
@contact: cailyn.song@isysful.com
@time: 2022/6/7 11:02
@file: search_page.py
@desc: 封装搜素页方法
"""
from common.base_page import BasePage


class Search(BasePage):
    def tap_search_icon(self):
        """
        点击搜索图标
        """
        self.click("id", "com.mimu.mshop:id/img_search", "搜索图标")

    def search(self, keyword):
        """
        输入关键字搜索
        :param keyword: 搜索关键字
        """
        self.tap_search_icon()
        self.input_data("id", "com.mimu.mshop:id/et_input", "输入搜索关键字", keyword)
        self.click("id", "com.mimu.mshop:id/tv_search", "搜索按钮")

    def history_search(self):
        """
        历史记录搜索
        """
        self.tap_search_icon()
        self.click("xpath",
                   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView",
                   "历史记录")

    def delete_history(self):
        """
        删除历史搜索记录
        """
        self.tap_search_icon()
        self.click("id", "com.mimu.mshop:id/iv_delete_history", "历史记录")
        el = self.get_attribute("id", "com.mimu.mshop:id/tv_history_empty", "删除历史搜索记录", "text")
        return el

    def hot_search(self):
        """
        热门搜索
        """
        self.tap_search_icon()
        self.click("xpath",
                   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView",
                   "热门搜索")

    def refresh_hot_search(self):
        """
        热门搜索
        """
        self.tap_search_icon()
        self.click("id", "com.mimu.mshop:id/tv_refresh", "换一换")
