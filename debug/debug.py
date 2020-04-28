# coding: utf-8
from appium import webdriver
from time import sleep

# 设备名
deviceName = '127.0.0.1:62001'

# 设备版本
platformVersion = '5.1.1'

desired_caps = {'platformName': 'Android',
                'deviceName': deviceName,
                'platformVersion': platformVersion,
                'appPackage': 'com.qiaqia',
                'appActivity': '.cardhome.activity.WelcomeActivity',
                'unicodeKeyboard': True,
                'resetKeyboard': True}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)
sleep(2)

try:
    # 点击我的去登录
    driver.find_element_by_id('com.qiaqia:id/id_bottom_person_icon').click()
    print("打开app成功去登录!!!")
except:
    print("打开app失败,运行关闭!!!")
    exit()
try:
    """ 登录 """
    # 输入手机号码
    driver.find_element_by_id('com.qiaqia:id/id_login_edit_phone_txt').send_keys('18295995951')
    # 点击切换密码登陆
    driver.find_element_by_id('com.qiaqia:id/id_login_tv_change').click()
    # 输入密码
    driver.find_element_by_id('com.qiaqia:id/id_login_edit_pwd_txt').send_keys('123456')
    # 查看密码
    driver.find_element_by_id('com.qiaqia:id/id_login_showpwd').click()
    # 点击登录
    driver.find_element_by_id('com.qiaqia:id/id_login_button').click()
    print("登录成功")
except:
    print("登录失败，运行关闭!!!")
    exit()
sleep(2)

try:
    """首页"""
    # 点击首页
    driver.find_element_by_id('com.qiaqia:id/id_bottom_home_bg').click()
    # 首页——消息
    try:
        # 点击消息
        driver.find_element_by_id('com.qiaqia:id/id_home_message').click()
        sleep(1)
        # 点击客服私聊页面
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                     '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                     '/android.support.v7.widget.LinearLayoutCompat/android.support.v4.view.ViewPager'
                                     '/android.widget.FrameLayout/android.view.View/android.support.v7.widget'
                                     '.RecyclerView/android.widget.FrameLayout/android.widget.RelativeLayout/android'
                                     '.widget.TextView[1]').click()
        sleep(1)
        # 点击返回
        driver.find_element_by_id('com.qiaqia:id/id_personal_chat_back').click()
        # 点击通知
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                     '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                     '/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout'
                                     '/android.widget.LinearLayout/android.widget.RelativeLayout['
                                     '2]/android.widget.LinearLayout/android.widget.TextView').click()
        # 点击搜索按钮
        driver.find_element_by_id('com.qiaqia:id/id_home_message_search').click()
        # 搜索框输入1
        driver.find_element_by_id('com.qiaqia:id/id_home_message_search_text').send_keys('1')
        sleep(3)
        # 点击私聊
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                     '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                     '/android.support.v7.widget.LinearLayoutCompat/android.widget.FrameLayout'
                                     '/android.widget.LinearLayout/android.widget.RelativeLayout['
                                     '1]/android.widget.LinearLayout/android.widget.TextView').click()
        # 清空搜索框内容
        driver.find_element_by_id('com.qiaqia:id/id_home_message_cancel_icon').click()
        # 点击取消
        driver.find_element_by_id('com.qiaqia:id/id_home_message_search_bar_cancel').click()
        # 返回首页)
        driver.find_element_by_id('com.qiaqia:id/id_message_back').click()
        print("消息执行完毕")
    except:
        print("消息执行失败")
    # 首页——搜索
    try:
        # 点击搜索
        driver.find_element_by_id('com.qiaqia:id/id_home_search').click()
        # 输入搜索内容
        driver.find_element_by_id('com.qiaqia:id/id_search_edit').send_keys('1')
        # 首页——搜索——群组
        try:
            # 点击群聊
            driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7'
                '.widget.LinearLayoutCompat/android.widget.FrameLayout['
                '2]/android.widget.LinearLayout/android.widget.RelativeLayout['
                '1]/android.widget.LinearLayout/android.widget.TextView').click()
            try:
                driver.find_element_by_id('com.qiaqia:id/btn_add').click()
                print("有可加入的群组，加群成功")
            except:
                print("没有可加入的群组")
        except:
            print("群组页面未能加载出来")
        try:
            # 点击内容
            driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7'
                '.widget.LinearLayoutCompat/android.widget.FrameLayout['
                '2]/android.widget.LinearLayout/android.widget.RelativeLayout['
                '2]/android.widget.LinearLayout/android.widget.TextView').click()
            try:
                driver.find_element_by_id('com.qiaqia:id/start_play').click()
                print("发现视频资源，点击播放")
                sleep(3)
                # 点击资源
                driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android'
                                             '.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.View'
                                             '/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout['
                                             '1]/android.widget.TextView[2]').click()
                sleep(3)
                try:
                    # 点击对应资源的喜欢
                    driver.find_element_by_id('com.qiaqia:id/id_item_video_content_unlike').click()
                    print("喜欢成功")
                except:
                    # 点击对应资源的不喜欢
                    driver.find_element_by_id('com.qiaqia:id/id_item_video_content_like').click()
                    print("取消喜欢成功")
                sleep(2)
                try:
                    # 点击对应资源的不收藏
                    driver.find_element_by_id('com.qiaqia:id/id_item_video_content_uncollect').click()
                    print("收藏成功")
                except:
                    # 点击对应资源的不收藏
                    driver.find_element_by_id('com.qiaqia:id/id_item_video_content_collect').click()
                    print("取消收藏成功")
                # 点击资源列表
                driver.find_element_by_id('com.qiaqia:id/id_item_res_content_goto_stagger').click()
                # 点击对应的资源
                driver.find_element_by_id('com.qiaqia:id/thumb').click()
                # 点击资源的跑马灯
                driver.find_element_by_id('com.qiaqia:id/id_item_content_marquee_content').click()
                # 如果要是有‘当前群组的专属客服。。。’
                try:
                    # 点击知道了
                    driver.find_element_by_id('com.qiaqia:id/tv_know').click()
                    print("第一次进入聊天页，弹框关闭成功")
                except:
                    print("第一次进入聊天页，弹框关闭失败")
                # 输入要发送的内容
                driver.find_element_by_id('com.qiaqia:id/ed_input').send_keys('sdasdsadasdsa')
                # 点击发送
                driver.find_element_by_id('com.qiaqia:id/btn_confirm').click()
                # 点击表情键盘
                driver.find_element_by_id('com.qiaqia:id/img_chat_emoji').click()
                # 点击要发送的表情
                driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout['
                                             '2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view'
                                             '.View/android.view.View[2]/android.view.View['
                                             '2]/android.support.v4.view.ViewPager/android.view.View/android.support'
                                             '.v7.widget.RecyclerView/android.view.View').click()
                # 点击发送
                driver.find_element_by_id('com.qiaqia:id/btn_confirm').click()
                # 点击发送语音(长按五秒)
                driver.find_element_by_id('com.qiaqia:id/img_record').click()
                # el = driver.find_element_by_id('com.qiaqia:id/btn_speak')
                # action.long_perss(el, duration=31000).wait(5000).perfrom()
                driver.swipe(255,910,255,910,5000)
                # 点击加号
                driver.find_element_by_id('com.qiaqia:id/img_chat_emoji_more').click()
                try:
                    # 点击照片
                    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                                 '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout['
                                                 '2]/android.widget.LinearLayout/android.widget.FrameLayout/android.view'
                                                 '.View/android.view.View['
                                                 '2]/android.support.v7.widget.RecyclerView/android.view.View['
                                                 '1]/android.widget.ImageView').click()
                    # 选择照片
                    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                                 '.FrameLayout/android.view.View/android.widget.GridView/android.widget'
                                                 '.FrameLayout[2]/android.view.View/android.widget.CheckBox').click()
                    # 点击完成
                    driver.find_element_by_id('com.qiaqia:id/btn_confirm').click()
                except:
                    # 点击取消
                    driver.find_element_by_id('com.qiaqia:id/btn_cancel').click()
            except:
                print("未发现视频资源，无法点击播放")
            try:
                # 点击投稿
                driver.find_element_by_id('com.qiaqia:id/id_personal_photo').click()
                # 输入投稿的标题
                driver.find_element_by_id('driver.find_element_by_id()').send_keys('dsadasdsadsa')
                # 输入分享说的话
                driver.find_element_by_id('com.qiaqia:id/ed_content').send_keys('sdfghjsa')
                # 点击添加照片
                driver.find_element_by_id('com.qiaqia:id/img_upload').click()
                # 手机相册选择
                driver.find_element_by_id('com.qiaqia:id/tv_photo').click()
                try:
                    try:
                        # 选择照片
                        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                     '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                                     '.FrameLayout/android.view.View/android.widget.GridView/android.widget'
                                                     '.FrameLayout[2]/android.view.View/android.widget.CheckBox').click()
                        # 点击完成
                        driver.find_element_by_id('com.qiaqia:id/btn_confirm').click()
                    except:
                        # 点击取消
                        driver.find_element_by_id('com.qiaqia:id/btn_cancel').click()
                    # 点击提交
                    driver.find_element_by_id('com.qiaqia:id/tv_submit').click()
                except:
                    # 点击返回
                    driver.find_element_by_id('com.qiaqia:id/img_back').click()
            except:
                # 点击关闭聊天页面
                driver.find_element_by_id('com.qiaqia:id/v_view').click()
                # 点击返回
                driver.find_element_by_id('com.qiaqia:id/id_item_res_content_back').click()
        except:
            print("内容页面未能加载出来")
        # 点击用户
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                     '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7'
                                     '.widget.LinearLayoutCompat/android.widget.FrameLayout['
                                     '2]/android.widget.LinearLayout/android.widget.RelativeLayout['
                                     '3]/android.widget.LinearLayout/android.widget.TextView').click()
        # 点击取消
        driver.find_element_by_id('com.qiaqia:id/id_search_cancel').click()
        print("搜索执行成功")
    except:
        print("搜索执行失败")
    # 首页——滑动群组
    try:
        # 滑动群组
        driver.swipe(470, 233, 70, 233, 1000)
        sleep(2)
        driver.swipe(470, 233, 70, 233, 1000)
        sleep(2)
        driver.swipe(470, 233, 70, 233, 1000)
        sleep(2)
        print("滑动群组执行成功")
    except:
        print("滑动群组执行失败")
    # 首页——收起展开群组
    try:
        # 点击缩小群组
        driver.find_element_by_id('com.qiaqia:id/id_home_banner_close').click()
        sleep(1)
        # 展开群组
        driver.find_element_by_id('com.qiaqia:id/id_home_banner_show').click()
        sleep(1)
        # 点击缩小群组
        driver.find_element_by_id('com.qiaqia:id/id_home_banner_close').click()
        print("收起展开群组执行成功")
    except:
        print("收起展开群组执行失败")
    # 首页——点击小头像切换群组
    try:
        # 点击头像切换群组(从右往左滑动一个)
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                     '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                     '.FrameLayout/android.widget.FrameLayout['
                                     '2]/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView'
                                     '/android.widget.RelativeLayout[4]/android.widget.ImageView').click()
        sleep(1)
        # 点击头像切换群组(从右往左滑动两个)
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                     '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                     '.FrameLayout/android.widget.FrameLayout['
                                     '2]/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView'
                                     '/android.widget.RelativeLayout[5]/android.widget.ImageView').click()
        sleep(1)
        # 点击头像切换群组(从左往右滑动一个)
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                     '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                     '.FrameLayout/android.widget.FrameLayout['
                                     '2]/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView'
                                     '/android.widget.RelativeLayout[2]/android.widget.ImageView').click()
        sleep(1)
        # 点击头像切换群组(从左往右滑动两个)
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                     '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                     '.FrameLayout/android.widget.FrameLayout['
                                     '2]/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView'
                                     '/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
        sleep(1)
        print("点击小头像切换群组执行成功")
    except:
        print("点击小头像切换群组执行失败")
    # 首页——点击对应群组的喜欢
    try:
        # 点击首页的喜欢按钮
        driver.find_element_by_id('com.qiaqia:id/img_un_like').click()
        # 点击返回到首页
        driver.find_element_by_id('com.qiaqia:id/id_item_res_content_back').click()
        # 点击首页跑马灯
        driver.find_element_by_id('com.qiaqia:id/id_item_content_marquee_content').click()
        sleep(2)
        # 点击返回到首页
        driver.find_element_by_id('com.qiaqia:id/id_item_res_content_back').click()
        print("点击对应群组的喜欢执行成功")
    except:
        print("点击对应群组的喜欢执行失败")
except:
    print("首页打开失败")