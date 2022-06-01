import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '10',  # 手机安卓版本
    'deviceName': '192.168.31.102:5555',  # 设备名，安卓手机可以随意填写
    'appPackage': ' tv.danmaku.bili',  # 启动APP Package名称
    'appActivity': '.MainActivityV2',  # 启动Activity名称
    'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    'noReset': True,  # 不要重置App
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 设置缺省等待时间
driver.implicitly_wait(20)

# 如果有`青少年保护`界面，点击`我知道了`

# 根据id定位搜索位置框，点击
time.sleep(4)
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="搜索栏，按钮")
el1.click()
time.sleep(3)
#
# # 根据id定位搜索输入框，点击
# sbox = driver.find_element(By.ID, 'tv.danmaku.bili:id/search_src_text')
# sbox.send_keys('白月黑羽')
# # 输入回车键，确定搜索
# driver.press_keycode(AndroidKey.ENTER)
#
# # 选择（定位）所有视频标题
# eles = driver.find_elements(By.ID, 'title')
#
# for ele in eles:
#     # 打印标题
#     print(ele.text)
#
# input('**** Press to quit..')
driver.quit()
