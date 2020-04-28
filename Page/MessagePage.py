"""消息页面"""

from Page.UiElements import UiElements
from Base.Base import Base


class MessagePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_message_btn(self,element):
        """点击消息按钮"""
        self.click_element(element)

    def click_private_btn(self):
        """点击私聊按钮"""
        self.click_element(UiElements.Message_private_btn_xpath)
        """客服私聊数据"""
        try:
            """点击客服私聊"""
            self.click_element(UiElements.Message_service_btn_xpath)
            """客服私聊页面返回"""
            self.click_element(UiElements.Message_personal_chat_back_btn_id)
        except:
            print("暂无与客服私聊数据")
            pass
    def click_inform_btn(self):
        """点击通知按钮"""
        self.click_element(UiElements.Message_inform_btn_xpath)

    def click_search_btn(self, txt):
        """点击搜索"""
        self.click_element(UiElements.Message_search_btn_id)
        """搜索框输入内容"""
        self.send_element(UiElements.Message_search_txt_id, txt)
        try:
            """点击私聊"""
            self.click_element(UiElements.Message_private_btn_xpath)
            """筛选以后，点击客服私聊页"""
            self.click_element(UiElements.Message_service_btn_xpath)
            """客服私聊页面返回"""
            self.click_element(UiElements.Message_personal_chat_back_btn_id)
        except:
            print("暂无与客服私聊数据")
            pass
        try:
            """点击通知"""
            self.click_element(UiElements.Message_inform_btn_xpath)
        except:
            print("暂无通知数据")
            pass
        """点击清空搜索框"""
        self.click_element(UiElements.Message_clear_search_btn_id)
        """点击取消"""
        self.click_element(UiElements.Message_cancel_search_btn_id)
        """点击客服私聊页面返回"""
        self.click_element(UiElements.Message_back_btn_id)