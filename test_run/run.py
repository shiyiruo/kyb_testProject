import unittest
import sys
path = 'D:\\mycode\\python\\appium_demo\\'
sys.path.append(path)
from kyb_testProject.common.BSTestRunner import BSTestRunner
import time
import logging

test_dir = '../test_case'
report_dir = '../report/'
# 加载用例
suite = unittest.defaultTestLoader.discover(test_dir)
# 定义报告文件名格式
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir+ now + ' test_report.html'

with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title= 'Test Report', description= 'kyb Andriod app Test Report')
    logging.info('start run testcase...')
    runner.run(suite)


