"""客服页面"""

from Base.Base import Base
from Page.UiElements import UiElements


class ServicePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_record_btn(self):
        try:
            """语音按钮"""
            self.click_element(UiElements.Resource_chat_record_btn_id)
            """按住说话"""
            self.click_element(UiElements.Resource_chat_btn_speak_btn_id)
            print("发送语音成功")
        except:
            print("发送语音失败")
            pass

    def send_input_txt(self, chat_input_txt):
        try:
            """请输入聊天内容"""
            self.send_element(UiElements.Resource_chat_input_txt_id, chat_input_txt)
            print("发送聊天内容成功")
        except:
            print("发送聊天内容失败")
            pass

    def click_emoji_btn(self):
        try:
            """表情按钮"""
            self.click_element(UiElements.Resource_chat_emoji_btn_id)
            """选择一个表情"""
            self.click_element(UiElements.Resource_chat_one_emoji_btn_xpath)
            """发送按钮"""
            self.click_element(UiElements.Resource_chat_send_btn_id)
            print("发送表情成功")
        except:
            print("发送表情失败")
            pass

    def click_photo_img(self):
        try:
            """展开（➕）"""
            self.click_element(UiElements.Resource_chat_emoji_more_btn_id)
            """选择照片"""
            self.click_element(UiElements.Resource_chat_photo_btn_xpath)
            """选择图片"""
            self.click_element(UiElements.Resource_chat_contribute_add_img_btn_xpath)
            """完成"""
            self.click_element(UiElements.Resource_chat_contribute_confirm_btn_id)
            print("发送图片成功")
        except:
            """取消"""
            self.click_element(UiElements.Resource_chat_contribute_close_confirm_btn_id)
            print("发送图片失败")

    def click_personal_chat_back_btn(self):
        """客服私聊页面返回"""
        self.click_element(UiElements.Message_personal_chat_back_btn_id)