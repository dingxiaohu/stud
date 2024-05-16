import unittest

from data.get_csv import get_csv
from dev.login import login


class Test_App(unittest.TestCase):
    def setUp(self):
        print("用例准备工作")
        # 获取数据
        data = get_csv("..\data\login.csv")
        self.data = data

    def tearDown(self):
        print("用例收尾工作")

    #正确账号密码登录
    def test_login01(self):
        login(self.data[0][0], self.data[0][1])

    #未注册账号和错误密码登录
    def test_login02(self):
        login(self.data[1][0], self.data[1][1])

