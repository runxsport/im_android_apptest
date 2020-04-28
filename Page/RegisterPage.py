"""注册页面"""

from Base.Base import Base
from Page.UiElements import UiElements


class RegisterPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def Register(self, phone, getcode, invent):
        """输入手机号码"""
        self.send_element(UiElements.Register_phone_txt_id, phone)
        """点击获取验证码"""
        self.click_element(UiElements.Register_getcode_btn_id)
        """输入验证码"""
        self.send_element(UiElements.Register_code_txt_id, getcode)
        """请输入邀请码"""
        self.send_element(UiElements.Register_invitecode_txt_id, invent)
        """点击注册"""
        self.click_element(UiElements.Register_register_btn)

    def register_close_page(self):
        """关闭注册页面"""
        # 点击关闭按钮
        self.click_element(UiElements.Register_back_btn_id)

    def if_register_btn(self):
        """判断注册按钮是否存在"""
        self.get_element(UiElements.Register_register_btn)

    def register_imlogin_btn(self):
        """点击立即登陆"""
        self.click_element(UiElements.Register_imlogin_btn_id)