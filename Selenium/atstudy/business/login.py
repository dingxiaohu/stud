import os.path

from config.dxh_driver import get_firefox_driver
from config.dxh_findelement import DxhFindElement
from test_data.read_csv import get_csv_data

'''
dxh_driver  启动浏览器返回的webdriver对象
username    登录的账户名
password    登录的密码
'''


# 登录 登录成功返回True 失败返回False
def login(dxh_driver, username, password):
    # 实例化一个用来获取元素的对象
    dxh = DxhFindElement(dxh_driver)
    node = "dxh_login"

    # 点击登录
    dxh.get_element(node=node, key="user_login").click()
    # 输入账号
    dxh.get_element(node=node, key="user_name").send_keys(username)
    # 输入密码
    dxh.get_element(node=node, key="user_password").send_keys(password)
    # 点击登录
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
