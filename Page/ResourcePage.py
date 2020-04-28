"""资源页面"""

from Base.Base import Base
from Page.UiElements import UiElements


class ResourcePage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_back_btn(self):
        """资源页返回"""
        self.click_element(UiElements.Resource_back_btn_id)

    def click_group_resource_btn(self):
        """点击群资源"""
        self.click_element(UiElements.Resource_group_brn_id)
        """群资源进入个人资源"""
        self.click_element(UiElements.Resource_group_user_btn_xpath)

    def click_like_btn(self):
        """资源喜欢、取消喜欢"""
        try:
            """资源喜欢"""
            self.click_element(UiElements.Resource_like_content_btn_id)
            print("资源喜欢成功")
        except:
            self.click_element(UiElements.Resource_nolike_content_btn_id)
            print("资源取消喜欢成功")

    def click_collect_btn(self):
        """资源收藏、取消收藏"""
        try:
            """资源收藏"""
            self.click_element(UiElements.Resource_collect_content_btn_id)
            print("资源收藏成功")
        except:
            """资源取消收藏"""
            self.click_element(UiElements.Resource_nocollect_content_btn_id)
            print("资源取消收藏成功")

    def click_add_group_btn(self):
        try:
            """资源加群"""
            self.click_element(UiElements.Resource_add_group_btn_id)
            print("资源加群成功")
        except:
            print("资源页面没有可加入的群")

    def click_chat_btn(self, Resource_chat_contribute_title, Resource_chat_contribute_content):
        try:
            """跑马灯"""
            self.click_element(UiElements.Resource_marquee_content_btn_id)
            print("进入资源聊天页面")
            try:
                """点击加群即可开始聊天"""
                self.click_element(UiElements.Resource_chat_click_add_group_btn_xpath)
                print("关闭‘点击加群即可开始聊天’弹框成功")
            except:
                print("没有‘点击加群即可开始聊天’弹框")
                pass
            try:
                """"当前群组的专属客服在此点击找ta聊天（点击知道了）"""
                self.click_element(UiElements.Resource_chat_message_service_btn_id)
                print("关闭‘当前群组的专属客服在此点击找ta聊天（点击知道了）’弹框成功")
            except:
                print("没有‘当前群组的专属客服在此点击找ta聊天（点击知道了）’弹框")
                pass
            try:
                """该群组未加入（加群）"""
                self.click_element(UiElements.Resource_chat_add_newgroup_btn_id)
                print("加入该群成功，可以聊天啦")
            except:
                print("该群组已加入，可以聊天啦")
                pass
            try:
                """点击投稿"""
                self.click_element(UiElements.Resource_chat_contribute_btn_id)
                """请输入标题"""
                self.send_element(UiElements.Resource_chat_contribute_title_btn_id, Resource_chat_contribute_title)
                """分享你要说的话"""
                self.send_element(UiElements.Resource_chat_contribute_content_btn_id, Resource_chat_contribute_content)
                """添加图片"""
                self.click_element(UiElements.Resource_chat_contribute_add_img_btn_id)
                """从手机相册选择"""
                self.click_element(UiElements.Resource_chat_contribute_photo_img_btn_id)
                try:
                    """选择图片"""
                    self.click_element(UiElements.Resource_chat_contribute_add_img_btn_xpath)
                    """完成"""
                    self.click_element(UiElements.Resource_chat_contribute_confirm_btn_id)
                except:
                    """取消"""
                    self.click_element(UiElements.Resource_chat_contribute_close_confirm_btn_id)
                    print("没有图片，投稿失败")
                """投稿提交"""
                self.click_element(UiElements.Resource_chat_contribute_submit_btn_id)
            except:
                """投稿返回"""
                self.click_element(UiElements.Resource_chat_contribute_back_btn_id)
                print("投稿失败")
        except:
            print("进入资源聊天页面失败")

    def click_service_btn(self):
        """客服悬浮球"""
        self.click_element(UiElements.Resource_chat_service_suspend_btn_id)

    def click_close_chat_btn(self):
        """关闭聊天框"""
        self.click_element(UiElements.Resource_chat_close_chat_btn_id)

    """调试"""
    def debug(self):
        try:
            """语音按钮"""
            self.click_element(UiElements.Resource_chat_record_btn_id)
            """按住说话"""
            self.click_element(UiElements.Resource_chat_btn_speak_btn_id)
            print("发送语音成功")
        except:
            print("发送语音失败")
            pass
        try:
            """请输入聊天内容"""
            self.send_element(UiElements.Resource_chat_input_txt_id)
            print("发送聊天内容成功")
        except:
            print("发送聊天内容失败")
            pass
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