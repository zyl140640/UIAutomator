# encoding: utf-8
"""
@author: 宋坤坤
@contact: cailyn.song@isysful.com
@time: 2022/6/6 17:18
@file: Navigation_Bar.py
@desc: 封装底部导航栏
"""
from common.base_page import BasePage


class NavigationBarPage(BasePage):
    """
    nav_main: 底部导航栏-首页
    nav_category: 底部导航栏-分类
    nav_find: 底部导航栏-发现
    nav_cart: 底部导航栏-购物车
    nav_my: 底部导航栏-我的
    """
    nav_main = ('id', 'com.mimu.mshop:id/homeFragment')
    nav_category = ('id', 'com.mimu.mshop:id/sortFragment')
    nav_find = ('id', 'com.mimu.mshop:id/findFragment')
    nav_cart = ('id', 'com.mimu.mshop:id/shopFragment')
    nav_my = ('id', 'com.mimu.mshop:id/mineFragment')
    # 首页金刚区-超市按钮
    main_page_vajra_market_icon = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView')
    # 首页金刚区-餐厅按钮
    main_page_restaurant_market_icon = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.ImageView')
    # 首页金刚区-门店按钮
    main_page_vajra_offline_icon = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.ImageView')
    # 首页金刚区-优惠券按钮
    main_page_vajra_coupon_icon = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.ImageView')
    # 首页金刚区-会员按钮
    main_page_vajra_vip_icon = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.ImageView')

    def main_nav(self):
        """
        点击底部导航栏首页
        """
        self.click(self.nav_main, '底部导航栏-首页')

    def category_nav(self):
        """
        点击底部导航栏分类
        """
        self.click(self.nav_category, '底部导航栏-分类')

    def find_nav(self):
        """
        点击底部导航栏发现
        """
        self.click(self.nav_find, '底部导航栏-发现')

    def cart_nav(self):
        """
        点击底部导航栏购物车
        """
        self.click(self.nav_cart, '底部导航栏-购物车')

    def my_nav(self):
        """
        点击底部导航栏我的
        """
        self.click(self.nav_my, '底部导航栏-我的')

    def enter_market_page(self):
        """
        点击首页超市按钮
        """
        self.click(self.main_page_vajra_market_icon, '点击首页超市按钮')

    def enter_restaurant_page(self):
        """
        点击首页餐厅按钮
        """
        self.click(self.main_page_restaurant_market_icon, '点击首页餐厅按钮')

    def enter_offline_page(self):
        """
        点击首页门店按钮
        """
        self.click(self.main_page_vajra_offline_icon, '点击首页门店按钮')

    def enter_coupon_page(self):
        """
        点击首页优惠券按钮
        """
        self.click(self.main_page_vajra_coupon_icon, '点击首页优惠券按钮')

    def enter_vip_page(self):
        """
        点击首页会员按钮
        """
        self.click(self.main_page_vajra_vip_icon, '点击首页会员按钮')
