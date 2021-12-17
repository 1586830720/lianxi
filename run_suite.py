import unittest
from htmltestreport import HTMLTestReport
from scripts.test_01 import login_api
from scripts.test_02 import TestStaffAPI
import config

suite = unittest.defaultTestLoader.loadTestsFromTestCase(login_api)
suite1 = unittest.defaultTestLoader.loadTestsFromTestCase(TestStaffAPI)
runner = HTMLTestReport(config.c+"/report/aaa.html",title="报告")
runner.run(suite)
runner.run(suite1)

