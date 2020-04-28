"""我的页面"""

from Page.UiElements import UiElements
from Base.Base import Base


class MyPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_my_btn(self):
        """点击我的按钮"""
        self.click_element(UiElements.My_page_btn_id)
