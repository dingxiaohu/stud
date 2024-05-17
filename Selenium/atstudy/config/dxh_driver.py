import os
from time import sleep

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service

from config.read_ini import DxhReadIni

# 工程路径
parent_path = os.path.dirname(os.path.dirname(__file__)) + "/browserdriver"
# 专门读取配置文件对象
dxh = DxhReadIni()
# 获取被测网站
url = dxh.get_value("url")


def get_firefox_driver():
    #获取驱动地址
    driver_path = parent_path + "/geckodriver.exe"
    ser = Service()
    ser.path = driver_path
    driver = webdriver.Firefox(service=ser)
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(3)
    sleep(3)
    return driver


# 启动Microsoft edge浏览器
def get_edge_driver():
    #获取驱动地址
    driver_path = parent_path + "/msedgedriver.exe"
    ser = Service()
    ser.path = driver_path
    driver = webdriver.Edge(service=ser)
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(3)
    sleep(3)
    return driver


# 启动Chrome谷歌浏览器
def get_chrome_driver():
    # 获取驱动地址
    driver_path = parent_path + "/chromedriver.exe"
    ser = Service()
    ser.path = driver_path
    driver = webdriver.Chrome(service=ser)
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(3)
    sleep(3)
    return driver


# 单元测试
if __name__ == '__main__':
    get_firefox_driver()
