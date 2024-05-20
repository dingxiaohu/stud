import os
from time import sleep

from selenium import webdriver

from config.dxh_driver import get_firefox_driver
from config.read_ini import DxhReadIni


class DxhFindElement:
    def __init__(self, driver):
        self.driver = driver

    # 获取元素
    def get_element(self, file=None, node=None, key=None):
        if file is None:
            file = os.path.dirname(os.path.dirname(__file__)) + "/business/LocalElement.ini"

        if node is None:
            node = "dxh_login"

        read_ini = DxhReadIni(file, node)
        data = read_ini.get_value(key)
        #得出定位方式 文件中是以 > 方式切割
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'class_name':
                return self.driver.find_element_by_class_name(value)
            elif by == 'link_text':
                return self.driver.find_element_by_link_text(value)
            elif by == 'xpath':
                print(2222)
                return self.driver.find_element_by_xpath(value)
            elif by == 'css':
                return self.driver.find_element_by_css_selector(value)
            elif by == 'tag_name':
                return self.driver.find_element_by_tag_name(value)
            elif by == 'partial_link_name':
                return self.driver.find_element_by_partial_link_name(value)
        except:
            return None

    def roll_bottom(self):
        self.driver.set_window_size(600, 600)
        sleep(2)
        #通过js设置浏览器窗口滚动条位置
        #横向滚到100
        #纵向滚到450
        js = "window.scrollTo(0,600);"
        self.driver.execute_script(js)


if __name__ == '__main__':
    file_path = os.path.dirname(os.path.dirname(__file__))+"/business/LocalElement.ini"
    aa = DxhFindElement(get_firefox_driver())
    yu = aa.get_element(file_path, "dxh_login", "user_login")
    sleep(2)
    print(yu)
