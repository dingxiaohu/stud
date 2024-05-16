import os.path

import yaml
from appium import webdriver


def my_driver():
    #获取yaml文件所在的目录
    yaml_dir = os.path.dirname(__file__)
    #获取yaml文件的完整目录
    yaml_path = os.path.join(yaml_dir, 'conf.yml')
    #打开yaml文件，读取内容
    content = open(yaml_path, 'r', encoding='utf-8')
    #解析yaml文件的内容(返回为一个字典)
    cap = yaml.load(content, Loader=yaml.FullLoader)

    #启动app（包含自动安装）
    return webdriver.Remote('http://localhost:4723/wd/hub', cap)
