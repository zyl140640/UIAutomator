# encoding: utf-8
"""
@author: 姜衍
@contact: zyl140640@163.com
@time: 2022/6/22 9:26
@file: goods_page.py
@desc: 
"""
from common.base_page import BasePage


class GoodsPage(BasePage):
    # 商品详情-商品关注
    goods_Favorite = ("id", "com.mimu.mshop:id/tv_collect")
    # 商品详情-商品-降价通知
    goods_Discount_Notice = ("id", "com.mimu.mshop:id/tv_discount")
    # 商品详情-商品规格弹框
    goods_Specification = ("id", "com.mimu.mshop:id/tv_spec")
    # 商品详情-商品优惠券列表
    goods_Coupon = ("id", "com.mimu.mshop:id/tv_coupon")
    # 商品添加到购物车按钮
    goods_addShop = ("id", "com.mimu.mshop:id/tv_shop_add")
    # 商品详情-立即购买
    goods_Buy = ("id", "com.mimu.mshop:id/tv_shop_buy")
    # 商品详情-店铺
    goods_Shop = ("id", "com.mimu.mshop:id/tv_shop")
    # 商品详情-客服
    goods_Service = ("id", "com.mimu.mshop:id/tv_service")
    # 列表内的商品
    goods_Shop_goods = ("id", "com.mimu.mshop:id/tv_name")

    def goods_add(self):
        self.time.sleep(2)
        self.get_text_click(("id", "com.mimu.mshop:id/tv_name"), "点击超市", "超市")
        self.time.sleep(2)
        self.click(self.goods_Coupon, "添加商品到购物车")
