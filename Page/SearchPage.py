"""搜索页面"""

from Base.Base import Base
from Page.UiElements import UiElements


class SearchPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_serch_btn(self, txt):
        """点击搜索按钮"""
        self.click_element(UiElements.Search_btn_id)
        """输入搜索文本"""
        self.send_element(UiElements.Search_txt_id, txt)

    def click_group_btn(self):
        """点击群组"""
        self.click_element(UiElements.Search_group_btn_xpath)
        """点击加群"""
        try:
            self.click_element(UiElements.Search_group_add_group_btn_xpath)
            print("有可加入的群组，加群成功")
        except:
            print("没有可加入的群组，加群失败")
            pass

    def click_content_btn(self):
        """点击内容"""
        self.click_element(UiElements.Search_content_btn_xpath)
        """点击播放资源"""
        try:
            self.click_element(UiElements.Search_content_start_play_ntm_id)
            print("有可播放的资源，播放成功")
            """点击进入资源"""
            try:
                self.click_element(UiElements.Search_content_start_resource_btn_xpath)
                print("查看资源的详细内容成功")
                # 点击返回
            except:
                print("查看资源的详细内容失败")
                pass
        except:
            print("没有可播放的资源，播放失败")
            pass

    def click_user_btn(self):
        """点击用户"""
        self.click_element(UiElements.Search_user_btn_xpath)
        try:
            """进入用户信息页面"""
            self.click_element(UiElements.Search_user_message_btn_xpath)
            print("成功进入用户信息页面")

            try:
                """点击菜单"""
                self.click_element(UiElements.Search_user_menu_btn_id)
                """点击举报"""
                self.click_element(UiElements.Search_user_report_btn_id)
                try:
                    """选择举报类型"""
                    self.click_element(UiElements.Search_report_type_btn_xpath)
                    """选择图片"""
                    self.click_element(UiElements.Search_report_add_img_btn_id)
                    """提交"""
                    self.click_element(UiElements.Search_report_submit_btn_id)
                    print("举报成功")
                except:
                    self.click_element(UiElements.Search_report_back_btn_id)
                    print("举报失败,返回")
            except:
                print("举报失败,返回")
                pass

            try:
                """点击拉黑"""
                self.click_element(UiElements.Search_user_black_btn_id)
                try:
                    """点击确定"""
                    self.click_element(UiElements.Search_black_confirm_id)
                except:
                    """点击取消"""
                    self.click_element(UiElements.Search_black_cancel_id)
            except:
                print("拉黑失败，返回")
                pass

            try:
                """点击用户关注"""
                self.click_element(UiElements.Search_user_attention_btn_id)
                print("关注成功")
            except:
                self.click_element(UiElements.Search_user_cancel_attention_btn_id)
                print("取消关注成功")
                pass

            try:
                """加入群组"""
                self.click_element(UiElements.Search_user_add_group_btn_xpath)
                print("加入群组成功")
            except:
                print("没有可加入的群组")
                pass

            try:
                """打开\关闭未展示群组"""
                self.click_element(UiElements.Search_user_show_group_btn_id)
                print("打开展示群组成功")
            except:
                self.click_element(UiElements.Search_publish_content_btn_xpath)
                print("关闭展示群组成功")

            try:
                """滑动屏幕"""
                self.scroll_sreen(1)
                try:
                    """查看全部"""
                    self.click_element(UiElements.Search_content_all_btn_id)
                    print("查看全部成功")
                    """发布的内容返回个人信息页"""
                    self.click_element(UiElements.Search_content_all_back_btn_id)
                except:
                    print("查看全部失败")
                    pass
                try:
                    """点击进入发布的内容资源页"""
                    self.click_element(UiElements.Search_content_resource_btn_xpath)
                    print("成功进入发布的内容资源页")
                    """发布的内容返回个人信息页"""
                    self.click_element(UiElements.Search_content_all_back_btn_id)
                except:
                    print("没有发布的内容")
                    pass
            except:
                print("没有发布的内容")
                pass
        except:
            print("未进入用户信息页面")
            pass
        """清空按钮"""
        self.click_element(UiElements.Search_clear_btn_id)
        """取消按钮"""
        self.click_element(UiElements.Search_cancel_btn_id)