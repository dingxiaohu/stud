import os


class DxhFindElement:
    def __init__(self, driver):
        self.driver = driver

    # 获取元素
    def get_element(self, file=None, node=None, key=None):
        if file is None:
            file = os.path.dirname(os.path.dirname(__file__)) + "/business/LocalElement.ini"

        if node is None:
            node = "jwlogin"
