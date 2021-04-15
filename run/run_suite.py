# encoding='utf-8'
# 导包
import unittest
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
from scripts.test01_login import TestLogin
import time
from tools.HwTestReport import HTMLTestReport

# 封装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))

# 指定测试报告路径
report = "../report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
# 文件流形式打开文件
with open(report, "wb+") as f:
    # 创建HTMLTestRunner运行器
    # runner = HTMLTestRunner(f, verbosity=2, description="测试结果如下", title = "tpshop登录接口测试报告")
    #
    # # 执行测试套件
    # runner.run(suite)

    # 创建HTMLTestRunner运行器
    runner = HTMLTestReport(f, description="测试结果如下", title="tpshop登录接口测试报告")

    # 执行测试套件
    runner.run(suite)
