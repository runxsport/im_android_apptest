"""消息页面"""

from Base.Base import Base
from Page.UiElements import UiElements


class LoginPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, phone, passwd):
        """切换密码登录"""
        self.click_element(UiElements.Login_change_pwd_btn_id)
        """输入手机号码"""
        self.send_element(UiElements.Login_phone_txt_id, phone)
        """输入登录密码"""
        self.send_element(UiElements.Login_password_btn_id, passwd)
        """点击登录"""
        self.click_element(UiElements.Login_login_btn_id)

    def login_close_page(self):
        """关闭登录页面"""
        self.click_element(UiElements.Login_back_btn_id)

    def if_login_btn(self):
        """判断登录按钮是否存在"""
        self.get_element(UiElements.Login_login_btn_id)