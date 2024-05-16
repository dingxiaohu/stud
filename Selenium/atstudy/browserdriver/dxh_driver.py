import os
from time import sleep

from selenium import webdriver

from config.read_ini import DXHReadIni

# 工程路径
parent_path = os.path.dirname(os.path.dirname(__file__))
# 专门读取配置文件对象
dxh = DXHReadIni()
# 获取被测网站
url = dxh.get_value("url")


def get_firefox_driver():
    #获取驱动地址
    #driver_path = parent_path + "/browserdriver/geckodriver"
    #driver = webdriver.Firefox(driver_path)
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(3)
    sleep(3)
    return driver


# 单元测试
if __name__ == '__main__':
    get_firefox_driver()
