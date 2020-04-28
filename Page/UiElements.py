"""所有元素"""

from selenium.webdriver.common.by import By


class UiElements:

    """三星系统权限"""
    Samsung_system_permission = (By.ID, "com.android.packageinstaller:id/permission_allow_button")

    """登录页面:(By.ID, "")、(By.XPATH, "")"""
    """关闭"""
    Login_back_btn_id = (By.ID, "com.qiaqia:id/id_login_back")
    """注册"""
    Login_register_btn_id = (By.ID, "com.qiaqia:id/id_login_tv_reg")
    """请输入手机号码"""
    Login_phone_txt_id = (By.ID, "com.qiaqia:id/id_login_edit_phone_txt")
    """请输入验证码"""
    Login_code_txt_id = (By.ID, "com.qiaqia:id/id_login_edit_code_txt")
    """请输入登录密码"""
    Login_password_btn_id = (By.ID, "com.qiaqia:id/id_login_edit_pwd_txt")
    """获取验证码"""
    Login_getcode_btn_id = (By.ID, "com.qiaqia:id/id_login_getcode")
    """切换密码登录"""
    Login_change_pwd_btn_id = (By.ID, "com.qiaqia:id/id_login_tv_change")
    """登录按钮"""
    Login_login_btn_id = (By.ID, "com.qiaqia:id/id_login_button")
    """用户协议勾选框"""
    Login_user_treaty_btn_id = (By.ID, "com.qiaqia:id/id_login_treaty_cb")
    """用户使用协议详情"""
    Login_user_treaty_details_btn_id = (By.ID, "com.qiaqia:id/id_login_treaty")

    """注册页面:(By.ID, "")、(By.XPATH, "")"""
    """请输入手机号码"""
    Register_phone_txt_id = (By.ID, "com.qiaqia:id/id_register_edit_phone_txt")
    """请输入验证码"""
    Register_code_txt_id = (By.ID, "com.qiaqia:id/id_register_edit_code_txt")
    """获取验证码"""
    Register_getcode_btn_id = (By.ID, "com.qiaqia:id/id_register_getcode")
    """请输入邀请码"""
    Register_invitecode_txt_id = (By.ID, "com.qiaqia:id/id_login_edit_phone_code_invent")
    """注册按钮"""
    Register_register_btn = (By.ID, "com.qiaqia:id/id_register_button")
    """用户协议勾选框"""
    Register_user_treaty_btn_id = (By.ID, "com.qiaqia:id/id_register_cb")
    """用户使用协议详情"""
    Register_user_treaty_details_btn_id = (By.ID, "	com.qiaqia:id/id_register_treaty")
    """立即登陆"""
    Register_imlogin_btn_id = (By.ID, "com.qiaqia:id/id_register_imlogin")
    """关闭注册页面"""
    Register_back_btn_id = (By.ID, "com.qiaqia: id / id_register_back")


    """首页的所有元素:(By.ID, "")、(By.XPATH, "")"""
    """首页按钮"""
    Home_page_btn_id = (By.ID, "com.qiaqia:id/id_bottom_home_bg")
    """获取首页标题"""
    Home_title_txt_id = (By.ID, "com.qiaqia:id/id_home_title")
    """消息按钮"""
    Home_message_btn_id = (By.ID, "com.qiaqia:id/id_home_message")
    """搜索按钮"""
    Home_search_btn_id = (By.ID, "com.qiaqia:id/id_home_search")
    """轮播图加群按钮"""
    Home_banner_add_group_btn_id = (By.ID, "com.qiaqia:id/id_home_banner_add_group")
    """关闭轮播图"""
    Home_close_banner_btn_id = (By.ID, "com.qiaqia:id/id_home_banner_close")
    """显示轮播图"""
    Home_show_banner_btn_id = (By.ID, "com.qiaqia:id/id_home_banner_show")
    """资源喜欢按钮"""
    Home_img_like_btn_id = (By.ID, "com.qiaqia:id/img_un_like")
    """资源跑马灯"""
    Home_mv_view_btn_id = (By.ID, "com.qiaqia:id/mv_view")
    """弹框加群"""
    Home_popout_add_group_btn_id = (By.ID, "	com.qiaqia:id/btn_add")
    """关闭弹框加群"""
    Home_close_popout_add_group_btn_id = (By.ID, "com.qiaqia:id/img_close")


    """我的页面元素:(By.ID, "")、(By.XPATH, "")"""
    """我的元素"""
    My_page_btn_id = (By.ID, "com.qiaqia:id/id_bottom_person_frame")


    """消息（公共方法）(By.ID, "")、(By.XPATH, "")"""
    """返回首页"""
    Message_back_btn_id = (By.ID, "com.qiaqia:id/id_message_back")
    """搜索按钮"""
    Message_search_btn_id = (By.ID, "com.qiaqia:id/id_home_message_search")
    """私聊按钮"""
    Message_private_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView")
    """通知按钮"""
    Message_inform_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView")
    """客服姓名按钮"""
    Message_service_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView[1]")
    """客服私聊页面返回"""
    Message_personal_chat_back_btn_id = (By.ID, "com.qiaqia:id/id_personal_chat_back")
    """搜索框请输入内容"""
    Message_search_txt_id = (By.ID, "com.qiaqia:id/id_home_message_search_text")
    """清空搜索框"""
    Message_clear_search_btn_id = (By.ID, "com.qiaqia:id/id_home_message_cancel_icon")
    """取消搜索"""
    Message_cancel_search_btn_id = (By.ID, "com.qiaqia:id/id_home_message_search_bar_cancel")


    """搜索(By.ID, "")、(By.XPATH, "")"""
    """搜索按钮"""
    Search_btn_id = (By.ID, "com.qiaqia:id/id_home_search")
    """请输入搜索内容"""
    Search_txt_id = (By.ID, "com.qiaqia:id/id_search_edit")
    """群组按钮"""
    Search_group_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView")
    """加群按钮"""
    Search_group_add_group_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.Button")
    """内容按钮"""
    Search_content_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView")
    """播放视频"""
    Search_content_start_play_ntm_id = (By.ID, "com.qiaqia:id/start_play")
    """进入资源"""
    Search_content_start_resource_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView[2]")
    """用户按钮"""
    Search_user_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.TextView")
    """进入用户信息页面"""
    Search_user_message_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.support.v7.widget.LinearLayoutCompat")
    """菜单按钮"""
    Search_user_menu_btn_id = (By.ID, "com.qiaqia:id/id_layout_client_pop")
    """举报按钮"""
    Search_user_report_btn_id = (By.ID, "com.qiaqia:id/id_menu_report")
    """举报类型"""
    Search_report_type_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.support.v7.widget.LinearLayoutCompat[1]/android.view.View/android.widget.TextView[1]")
    """添加图片"""
    Search_report_add_img_btn_id = (By.ID, "com.qiaqia:id/img_upload")
    """提交"""
    Search_report_submit_btn_id = (By.ID, "com.qiaqia:id/id_report_submit")
    """返回"""
    Search_report_back_btn_id = (By.ID, "com.qiaqia:id/img_back")
    """拉黑按钮"""
    Search_user_black_btn_id = (By.ID, "com.qiaqia:id/id_menu_black_name")
    """拉黑确定"""
    Search_black_confirm_id = (By.ID, "com.qiaqia:id/id_personal_black_pop")
    """拉黑取消"""
    Search_black_cancel_id = (By.ID, "com.qiaqia:id/id_personal_black_pop_cancel")
    """返回搜索页面"""
    Search_user_client_back_btn_id = (By.ID, "com.qiaqia:id/id_client_back")
    """关注按钮"""
    Search_user_attention_btn_id = (By.ID, "com.qiaqia:id/id_client_rl_unfocus")
    """取消关注"""
    Search_user_cancel_attention_btn_id = (By.ID, "com.qiaqia: id / id_client_rl_focus")
    """用户加入的群（未加群展示加群按钮）"""
    Search_user_add_group_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout[2]/android.support.v7.widget.LinearLayoutCompat/android.support.v7.widget.LinearLayoutCompat[1]/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.support.v7.widget.LinearLayoutCompat[1]/android.widget.RelativeLayout/android.widget.Button")
    """打开\关闭未展示群组"""
    Search_user_show_group_btn_id = (By.ID, "com.qiaqia:id/view_expan")
    """点击发布的内容"""
    Search_publish_content_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout[2]/android.support.v7.widget.LinearLayoutCompat/android.support.v7.widget.LinearLayoutCompat[2]/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.ImageView[1]")
    """查看全部"""
    Search_content_all_btn_id = (By.ID, "com.qiaqia:id/id_layout_client_content_all")
    """点击进入发布的内容资源页"""
    Search_content_resource_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.view.View/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.ImageView")
    """发布的内容返回个人信息页"""
    Search_content_all_back_btn_id = (By.ID, "com.qiaqia:id/id_item_res_list_back")
    """清空按钮"""
    Search_clear_btn_id = (By.ID, "com.qiaqia:id/id_search_cancel_icon")
    """取消按钮"""
    Search_cancel_btn_id = (By.ID, "com.qiaqia:id/id_search_cancel")


    """资源页面（公共方法）(By.ID, "")、(By.XPATH, "")"""
    """资源返回"""
    Resource_back_btn_id = (By.ID, "com.qiaqia:id/id_item_res_content_back")
    """群资源"""
    Resource_group_brn_id = (By.ID, "com.qiaqia:id/id_item_res_content_goto_stagger")
    """群资源返回"""
    Resource_group_back_btn_id = (By.ID, "com.qiaqia: id / id_item_res_list_back")
    """群资源进入个人资源"""
    Resource_group_user_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.view.View/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView[1]")
    """资源喜欢"""
    Resource_like_content_btn_id = (By.ID, "com.qiaqia:id/id_item_video_content_unlike")
    """资源取消喜欢"""
    Resource_nolike_content_btn_id = (By.ID, "com.qiaqia:id/id_item_video_content_like")
    """资源收藏"""
    Resource_collect_content_btn_id = (By.ID, "com.qiaqia:id/id_item_video_content_uncollect")
    """资源取消收藏"""
    Resource_nocollect_content_btn_id = (By.ID, "com.qiaqia:id/id_item_video_content_collect")
    """资源加群"""
    Resource_add_group_btn_id = (By.ID, "com.qiaqia:id/id_item_content_join")
    """跑马灯"""
    Resource_marquee_content_btn_id = (By.ID, "com.qiaqia:id/id_item_content_marquee_content")
    """点击加群即可开始聊天"""
    Resource_chat_click_add_group_btn_xpath = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.TextView")
    """当前群组的专属客服在此点击找ta聊天（点击知道了）"""
    Resource_chat_message_service_btn_id = (By.ID, "com.qiaqia:id/tv_know")
    """该群组未加入（加群）"""
    Resource_chat_add_newgroup_btn_id = (By.ID, "com.qiaqia:id/lin_res_group")
    """投稿"""
    Resource_chat_contribute_btn_id = (By.ID, "com.qiaqia:id/iv_res_publish")
    """投稿返回"""
    Resource_chat_contribute_back_btn_id = (By.ID, "com.qiaqia:id/img_back")
    """投稿提交"""
    Resource_chat_contribute_submit_btn_id = (By.ID, "com.qiaqia:id/tv_submit")
    """请输入标题"""
    Resource_chat_contribute_title_btn_id = (By.ID, "com.qiaqia:id/ed_title")
    """分享你要说的话"""
    Resource_chat_contribute_content_btn_id = (By.ID, "com.qiaqia:id/ed_content")
    """添加图片"""
    Resource_chat_contribute_add_img_btn_id = (By.ID, "com.qiaqia:id/img_upload")
    """拍摄"""
    Resource_chat_contribute_camera_btn_id = (By.ID, "	com.qiaqia:id/tv_camera")
    """从手机相册选择"""
    Resource_chat_contribute_photo_img_btn_id = (By.ID, "com.qiaqia:id/tv_photo")
    """选择图片"""
    Resource_chat_contribute_add_img_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.GridView/android.widget.FrameLayout[1]/android.view.View/android.widget.ImageView")
    """取消"""
    Resource_chat_contribute_close_confirm_btn_id = (By.ID, "com.qiaqia:id/btn_cancel")
    """完成"""
    Resource_chat_contribute_confirm_btn_id = (By.ID, "com.qiaqia:id/btn_confirm")
    """关闭聊天框"""
    Resource_chat_close_chat_btn_id = (By.ID, "com.qiaqia:id/v_view")
    """客服悬浮球"""
    Resource_chat_service_suspend_btn_id = (By.ID, "com.qiaqia:id/cv_head")
    """语音按钮"""
    Resource_chat_record_btn_id = (By.ID, "com.qiaqia:id/img_record")
    """按住说话"""
    Resource_chat_btn_speak_btn_id = (By.ID, "com.qiaqia:id/btn_speak")
    """请输入聊天内容"""
    Resource_chat_input_txt_id = (By.ID, "com.qiaqia:id/ed_input")
    """表情按钮"""
    Resource_chat_emoji_btn_id = (By.ID, "com.qiaqia:id/img_chat_emoji")
    """选择一个表情"""
    Resource_chat_one_emoji_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View[2]/android.view.View[2]/android.support.v4.view.ViewPager/android.view.View/android.support.v7.widget.RecyclerView/android.view.View")
    """发送按钮"""
    Resource_chat_send_btn_id = (By.ID, "com.qiaqia:id/btn_confirm")
    """展开（➕）"""
    Resource_chat_emoji_more_btn_id = (By.ID, "com.qiaqia:id/img_chat_emoji_more")
    """选择照片"""
    Resource_chat_photo_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View[2]/android.support.v7.widget.RecyclerView/android.view.View[1]/android.widget.ImageView")
    """选择拍摄"""
    Resource_chat_shoot_btn_xpath = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View[2]/android.support.v7.widget.RecyclerView/android.view.View[2]/android.widget.ImageView")