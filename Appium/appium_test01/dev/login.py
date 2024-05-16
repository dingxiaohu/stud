from appium.webdriver.common.appiumby import AppiumBy

from config.confi import my_driver
from data.get_csv import get_csv


def login(user, password):
    #安装并启动app
    driver = my_driver()
    driver.implicitly_wait(10)
    #点击账号
    driver.find_elements(AppiumBy.ID, "com.atstudy.ando:id/ivImg")[2].click()
    #点击登录
    driver.find_element(AppiumBy.XPATH, '//*[@text="点击登录/注册"]').click()
    #输入手机号
    driver.find_element(AppiumBy.ID, "com.atstudy.ando:id/et_account").send_keys(user)
    #输入密码
    driver.find_element(AppiumBy.ID, "com.atstudy.ando:id/et_password").send_keys(password)
    driver.find_element(AppiumBy.ID, "com.atstudy.ando:id/btn_login").click()
