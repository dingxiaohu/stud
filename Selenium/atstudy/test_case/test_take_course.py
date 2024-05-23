import os
import sys
import warnings

from business.login import login
from business.take_course import dxh_take_course
from config.dxh_driver import get_firefox_driver
from test_data.read_csv import get_csv_data

sys.path.append("..")

import unittest


class TestTakeCourse(unittest.TestCase):

    def setUp(self):
        print("测试准备工作")
        # 忽略ResourceWaring异常警告
        warnings.simplefilter("ignore", ResourceWarning)
        # 启动浏览器
        driver = get_firefox_driver()
        # 获取当前文件路径
        path = os.path.dirname(os.path.dirname(__file__))
        # 登录数据文件位置
        login_data_path = path+"/test_data/login.csv"
        # 课程相关元素位置
        course_path = path+"/business/LocalElement.ini"
        # 获取csv文件中的数据，返回一个字典
        login_dict = get_csv_data(login_data_path)
        self.course_path = course_path
        self.login_dict = login_dict
        self.driver = driver

    def tearDown(self):
        print("测试结束工作")
        self.driver.quit()

    def test_take_course01(self):
        print("第一条测试用例")
        login(self.driver, self.login_dict[1][0], self.login_dict[1][1])
        self.assertTrue(dxh_take_course(self.driver, self.course_path, self.login_dict[1][2]))

    def test_take_course02(self):
        print("第二条测试用例")
        login(self.driver, self.login_dict[2][0], self.login_dict[2][1])
        self.assertTrue(dxh_take_course(self.driver, self.course_path, self.login_dict[2][2]))

    def test_take_course03(self):
        print("第三条测试用例")
        login(self.driver, self.login_dict[3][0], self.login_dict[3][1])
        self.assertTrue(dxh_take_course(self.driver, self.course_path, self.login_dict[3][2]))


if __name__ == '__main__':
    unittest.main()
