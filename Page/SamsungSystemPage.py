"""三星系统权限弹框"""

from Base.Base import Base
from Page.UiElements import UiElements


class SamsungSystemPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_Samsung_system_permission(self):
        """关闭弹框"""
        try:
            self.click_element(UiElements.Samsung_system_permission)
            try:
                self.click_element(UiElements.Samsung_system_permission)
                try:
                    self.click_element(UiElements.Samsung_system_permission)
                except:
                    pass
            except:
                pass
        except:
            pass