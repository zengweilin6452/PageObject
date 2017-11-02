# -*- coding: utf-8 -*-

import unittest
import time
from Pages.loginPage import LoginPage
import csv
from selenium import webdriver


"""
    本登录界面测试用例需要在Datas/login_data.csv中设置以下三个参数：
        1)第一行第一列：username, 用户名，字符串类型， 格式如’admin‘;
        2)第一行第二列：password, 密码，字符串类型， 格式如’123456‘;
        3)第一行第三列：checktword, 检查语，字符串类型, 格式如’用户名一栏为空‘
"""


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        file = open(r'../Datas/login_data.csv', 'r')
        csv_data = csv.reader(file)
        cls.data = [rows for rows in csv_data]
        file.close()

        cls.driver = webdriver.Chrome()
        cls.url = 'http://******************************'
        cls.loginPage = LoginPage(cls.driver, cls.url)
        cls.loginPage.open_url()

    def setUp(self):
        time.sleep(1)

    def tearDown(self):
        self.loginPage.save_screen(self.loginPage.get_step_name())
        self.loginPage.open_url()

    @classmethod
    def tearDownClass(cls):
        cls.loginPage.quit()

    # 登录用例1：输入正确用户名和正确密码
    def test_login1_correct(self):
        self.loginPage.input_username(self.data[1][0])
        self.loginPage.input_passwd(self.data[1][1])
        self.loginPage.click_btn()
        actu_text = self.loginPage.actual_text(self.loginPage.correct_loc)
        self.assertIn(self.data[1][2], actu_text)

    # 登录用例2：输入正确用户名和错误密码
    def test_login2_pdwrong(self):
        self.loginPage.input_username(self.data[2][0])
        self.loginPage.input_passwd(self.data[2][1])
        self.loginPage.click_btn()
        self.assertTrue(self.loginPage.find(self.loginPage.error_loc))
        actu_text = self.loginPage.actual_text(self.loginPage.error_loc)
        self.assertIn(self.data[2][2], actu_text)

    # 登录用例3：用户名为空，密码输入正确
    def test_login3_noun(self):
        self.loginPage.input_username(self.data[3][0])
        self.loginPage.input_passwd(self.data[3][1])
        self.loginPage.click_btn()
        self.assertTrue(self.loginPage.find(self.loginPage.error_loc))
        actu_text = self.loginPage.actual_text(self.loginPage.error_loc)
        self.assertIn(self.data[3][2], actu_text)

    # 登录用例4：密码为空，用户名输入正确
    def test_login4_nopd(self):
        self.loginPage.input_username(self.data[4][0])
        self.loginPage.input_passwd(self.data[4][1])
        self.loginPage.click_btn()
        self.assertTrue(self.loginPage.find(self.loginPage.error_loc))
        actu_text = self.loginPage.actual_text(self.loginPage.error_loc)
        self.assertIn(self.data[4][2], actu_text)

