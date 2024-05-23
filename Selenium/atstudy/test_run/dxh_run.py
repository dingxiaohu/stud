# 指定测试用例和测试报告的路径
import time
import unittest

from test_run.BSTestRunner import BSTestRunner

test_dir = '../test_case'
report_dir = '../reports'
# 匹配测试多条用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
# 定义报告的格式
now = time.strftime("%Y-%m-%d-%H-%M-%S")
report_name = report_dir+"/"+now+"test_report.html"
# 运行用例并生成测试报告
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title="我的选课测试报告", description="我的选课功能测试报告")
    runner.run(discover)
