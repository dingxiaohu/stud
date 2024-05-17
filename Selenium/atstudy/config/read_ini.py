import configparser
import os


class DxhReadIni:
    #初始化路径
    #参数1 file_name 指定文件文件名
    #参数2 node 指定所需要的节点名
    def __init__(self, file_name=None, node=None):
        self.file_name = file_name
        self.node = node
        if file_name is None:
            #文件名 加r 防止自动转义
            self.file_name = os.path.dirname(os.path.dirname(__file__)) + "/config/confing.ini"
        if node is None:
            self.node = "DXH_config"
        self.cf = self.load_ini(self.file_name)

    #加载配置文件
    @staticmethod
    def load_ini(file_name):
        #获取解析配置对象
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding="utf-8")
        return cf

    #获取配置文件中的内容-->指定key
    def get_value(self, key):
        return self.cf.get(self.node, key)


# 单元测试
if __name__ == '__main__':
    aa = DxhReadIni()
    print(aa.get_value("browser"))
