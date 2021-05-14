# -*- coding: utf-8 -*-
# @Time : 2021/3/8 16:30
# @Author : Mr.WANG
# @Version : 
# @Function :程序启动入口
import time
import unittest
from unittests.pages.logpage import Log
from unittests.pages.CSVpage import testcasepath, reportpath
from HTMLTestRunner import HTMLTestRunner

# 获取当前日期时间
t = time.strftime('%Y-%m-%d %H时%M分%S秒', time.localtime())
f = open(reportpath + '/' + t + '.html', 'wb')
# 加载测试用例
cases = unittest.defaultTestLoader.discover(testcasepath, pattern='loginpage.py')
# 创建运行对象
runner = HTMLTestRunner(stream=f, verbosity=2, title='获取token', description='用例执行情况统计')
# 执行测试
runner.run(cases)
# 关闭文件
f.close()
