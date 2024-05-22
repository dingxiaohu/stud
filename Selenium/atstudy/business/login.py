import os.path

from config.dxh_driver import get_firefox_driver
from config.dxh_findelement import DxhFindElement
from test_data.read_csv import get_csv_data


# 登录
def login(dxh_driver, username, password):
    dxh = DxhFindElement(dxh_driver)
    node = "dxh_login"
    dxh.get_element(node=node, key="user_login").click()
    dxh.get_element(node=node, key="user_name").send_keys(username)
    dxh.get_element(node=node, key="user_password").send_keys(password)
    dxh.get_element(node=node, key="login_button").click()


if __name__ == '__main__':
    csv_file = os.path.dirname(os.path.dirname(__file__)) + "/test_data/login.csv"
    dxh_dict = get_csv_data(csv_file)
    driver = get_firefox_driver()
    login(driver, dxh_dict[1][0], dxh_dict[1][1])
    # for i in dxh_dict:
    #     driver = get_firefox_driver()
    #     login(driver, dxh_dict[i][0], dxh_dict[i][1])
    #     driver.quit()
