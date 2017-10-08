#  -*- coding:utf-8 -*-

import unittest
from HTMLTestRunner import HTMLTestRunner
import time

test_cases = unittest.defaultTestLoader.discover(r"./TestCase/", pattern='test_*.py')
time_str = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
file_name = r"./Reports/PageObejct_" + time_str + ".html"
file = open(file_name, 'wb')
runner = HTMLTestRunner(
        stream=file,
        title=u'Testcases with PageObject',
        description=u'Some Testcases!'
    )
runner.run(test_cases)
file.close()