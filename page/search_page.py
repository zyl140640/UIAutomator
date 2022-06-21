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
    # 搜索图标
    search_icon = ("id", "com.mimu.mshop:id/img_search")
    # 扫一扫图标
    scan_icon = ("id", "com.mimu.mshop:id/iv_scan")
    # 搜索输入框
    search_input_box = ("id", "com.mimu.mshop:id/et_input")
    # 搜索按钮
    search_button = ("id", "com.mimu.mshop:id/tv_search")
    # 搜索历史
    search_history = ("xpath",
                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView")
    # 删除历史记录
    delete_history = ("id", "com.mimu.mshop:id/iv_delete_history")
    # 删除历史搜索记录
    delete_history_text = ("id", "com.mimu.mshop:id/tv_history_empty")
    # 热点搜索
    hot_search = ("xpath",
                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView")
    # 换一换
    hot_search_refresh = ("id", "com.mimu.mshop:id/tv_refresh")
    def tap_search_icon(self):
        """
        点击搜索图标
        """
        self.click(self.search_icon, "搜索图标")

    def scan(self):
        """
        扫一扫
        """
        self.tap_search_icon()
        self.click(self.scan_icon, "扫一扫")

    def search(self, keyword):
        """
        输入关键字搜索
        :param keyword: 搜索关键字
        """
        self.tap_search_icon()
        self.input_data(self.search_input_box, "输入搜索关键字", keyword)
        self.click(self.search_button, "搜索按钮")

    def history_search(self):
        """
        历史记录搜索
        """
        self.tap_search_icon()
        self.click(self.search_history, "历史记录")

    def history_delete(self):
        """
        删除历史搜索记录
        """
        self.tap_search_icon()
        self.click(self.delete_history, "历史记录")
        el = self.get_attribute(self.delete_history_text, "删除历史搜索记录", "text")
        return el

    def search_hot(self):
        """
        热门搜索
        """
        self.tap_search_icon()
        self.click(self.hot_search, "热门搜索")

    def refresh_hot_search(self):
        """
        热门搜索
        """
        self.tap_search_icon()
        self.click(self.hot_search_refresh, "换一换")
