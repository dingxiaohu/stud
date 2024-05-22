import os
from time import sleep

from selenium.webdriver.common.by import By

from business.login import login
from config.dxh_driver import get_firefox_driver
from config.dxh_findelement import DxhFindElement
from test_data.read_csv import get_csv_data


# 登录成功才能选课
def dxh_take_course(dxh_driver, file_path, course_id):
    try:
        dxh = DxhFindElement(dxh_driver)
        node = "dxh_take_course"
        # dxh.get_element(file, node, "head_photo").click()
        # dxh.get_element(file, node, "learning_center").click()
        dxh.get_element(file_path, node, "course_center").click()
        sleep(1)
        dxh.get_element(file_path, node, "price_sort").click()
        sleep(1)
        dxh.get_element(file_path, node, "price_sort").click()
        sleep(1)
        course_xpath = "//*[@id='__layout']/div/div[2]/div/div[2]/div[2]/div[" + str(course_id) + "]/div[3]/button"
        dxh_driver.find_element(By.XPATH, course_xpath).click()
        sleep(1)
        dxh.get_element(file_path, node, "start_learn").click()
        sleep(1)
        result = dxh.get_element(file_path, node, "verify")
        sleep(1)
        print("找回复是否有评价的结果是", result)
        if result is None:
            return False
        else:
            return True
    except Exception as e:
        print("DXH", e)
        print("交流异常，都认为选课失败")
        return False
    finally:
        dxh_driver.quit()


if __name__ == '__main__':
    file = os.path.dirname(os.path.dirname(__file__)) + "/business/LocalElement.ini"
    csv_file = os.path.dirname(os.path.dirname(__file__)) + "/test_data/login.csv"
    dxh_dict = get_csv_data(csv_file)
    for i in dxh_dict:
        driver = get_firefox_driver()
        login(driver, dxh_dict[i][0], dxh_dict[i][1])
        dxh_take_course(driver, file, dxh_dict[i][2])
