"""启动app基本参数"""
from appium import webdriver


# 定义一个设备（版本：platformVersion,设备名：deviceName,包名：appPackage, 启动名：appActivity）
def get_phone_driver(platformVersion,deviceName,appPackage, appActivity):
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = platformVersion
    desired_caps['deviceName'] = deviceName
    # app的信息
    desired_caps['appPackage'] = appPackage
    desired_caps['appActivity'] = appActivity
    # 中文输入
    desired_caps['resetKeyboard'] = True
    desired_caps['unicodeKeyboard'] = True
    # 声明我们的driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)