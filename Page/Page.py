"""所有页面实例化参数（统一入口）"""


from Page.SamsungSystemPage import SamsungSystemPage
from Page.LoginPage import LoginPage
from Page.HomePage import HomePage
from Page.MessagePage import MessagePage
from Page.RegisterPage import RegisterPage
from Page.MyPage import MyPage
from Page.SearchPage import SearchPage
from Page.ServicePage import ServicePage
from Page.ResourcePage import ResourcePage

class Page:

    def __init__(self, driver):
        self.driver = driver

    def get_SamsungSystemPage(self):
        """返回注册实例化对象"""
        return SamsungSystemPage(self.driver)

    def get_RegisterPage(self):
        """返回注册实例化对象"""
        return RegisterPage(self.driver)

    def get_LoginPage(self):
        """返回登录页实例化对象"""
        return LoginPage(self.driver)

    def get_HomePage(self):
        """返回首页实例化对象"""
        return HomePage(self.driver)

    def get_MessagePage(self):
        """返回消息页面实例化对象"""
        return MessagePage(self.driver)

    def get_SearchPage(self):
        """返回消息页面实例化对象"""
        return SearchPage(self.driver)

    def get_MyPage(self):
        """返回消息页面实例化对象"""
        return MyPage(self.driver)

    def get_ServicePage(self):
        """返回消息页面实例化对象"""
        return ServicePage(self.driver)

    def get_ResourcePage(self):
        """返回消息页面实例化对象"""
        return ResourcePage(self.driver)