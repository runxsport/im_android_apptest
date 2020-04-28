"""首页"""

from Page.UiElements import UiElements
from Base.Base import Base


class HomePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_home_btn(self):
        """点击首页按钮"""
        self.click_element(UiElements.Home_page_btn_id)

    def click_banner_add_group_btn(self):
        """轮播图添加群组"""
        self.click_element(UiElements.Home_banner_add_group_btn_id)

    def click_close_banner_btn(self):
        """关闭轮播图"""
        self.click_element(UiElements.Home_close_banner_btn_id)

    def click_show_banner_btn(self):
        """显示轮播图"""
        self.click_element(UiElements.Home_show_banner_btn_id)

    def click_img_like_btn(self):
        """点击资源的喜欢按钮"""
        self.click_element(UiElements.Home_img_like_btn_id)

    def click_mv_view_btn(self):
        """点击跑马灯"""
        self.click_element(UiElements.Home_mv_view_btn_id)

    def swipe_img_add_group(self):
        """滑动屏幕"""
        self.scroll_sreen(1)

    def click_popout_add_group_btn(self):
        """点击弹框加群"""
        self.click_element(UiElements.Home_popout_add_group_btn_id)

    def click_close_popout_add_group_btn(self):
        """点击弹框加群"""
        self.click_element(UiElements.Home_close_popout_add_group_btn_id)

    def click_message_btn(self):
        """点击消息"""
        self.click_element(UiElements.Home_message_btn_id)