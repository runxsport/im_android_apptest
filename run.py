# coding: utf-8
from time import sleep
from Page.Page import Page
from Base.getdriver import get_phone_driver
from Page.UiElements import UiElements


"""定义一个设备（版本：platformVersion,设备名：deviceName,包名：appPackage, 启动名：appActivity）"""
driver = get_phone_driver('5.1.1','127.0.0.1:62001','com.qiaqia','.cardhome.activity.WelcomeActivity')
# driver = get_phone_driver('9','9889d6483158465037','com.qiaqia','.cardhome.activity.WelcomeActivity')
page_obj = Page(driver)

"""关闭三星权限弹框"""
# page_obj.get_SamsungSystemPage().click_Samsung_system_permission()

"""点击消息按钮，跳转到登陆页面"""
try:
    page_obj.get_MyPage().click_my_btn()
    print("跳转登录页成功")
except:
    print("跳转登录页失败")
    exit()

"""登录"""
try:
    page_obj.get_LoginPage().login("18295995951", "123456")
    print("登录成功")
except:
    print("登录失败")
    exit()

"""消息"""
page_obj.get_MessagePage().click_message_btn(UiElements.Home_message_btn_id)
page_obj.get_MessagePage().click_private_btn()
page_obj.get_MessagePage().click_inform_btn()
page_obj.get_MessagePage().click_search_btn("1")

"""搜索"""
page_obj.get_SearchPage().click_serch_btn("1")
page_obj.get_SearchPage().click_content_btn()
page_obj.get_ResourcePage().click_group_resource_btn()
page_obj.get_ResourcePage().click_like_btn()
page_obj.get_ResourcePage().click_collect_btn()
page_obj.get_ResourcePage().click_add_group_btn()
page_obj.get_ResourcePage().click_chat_btn("撒大苏打实打实","大苏打实打实")

page_obj.get_ServicePage().click_record_btn()
page_obj.get_ServicePage().send_input_txt("1")
page_obj.get_ServicePage().click_emoji_btn()
page_obj.get_ServicePage().click_photo_img()
page_obj.get_ServicePage().click_personal_chat_back_btn()

page_obj.get_ResourcePage().click_service_btn()

page_obj.get_ServicePage().click_record_btn()
page_obj.get_ServicePage().send_input_txt("1")
page_obj.get_ServicePage().click_emoji_btn()
page_obj.get_ServicePage().click_photo_img()
page_obj.get_ServicePage().click_personal_chat_back_btn()




page_obj.get_ResourcePage().click_close_chat_btn()
page_obj.get_SearchPage().click_user_btn()