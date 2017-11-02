#  -*- coding:utf-8 -*-

from Pages.postPage import PostPage
from selenium import webdriver
import time
import unittest
import csv

"""
    本登录界面测试用例需要在Datas/post_data.csv中设置以下三个参数：
        1)第一行第一列：title, 用户名，字符串类型， 格式如’hello‘;
        2)第一行第二列：article, 密码，字符串类型， 格式如’hello,world‘;
        3)第一行第三列：checktword, 检查语，字符串类型, 格式如’hello‘
"""


class TestPost(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        file = open(r"E:/python/PageObject/Datas/post_data.csv", 'r')
        csv_data = csv.reader(file)
        cls.data = [rows for rows in csv_data]
        file.close()

        cls.driver = webdriver.Chrome()
        cls.base_url = r"http://localhost:4466/wordpress/wp-admin"
        cls.postPage = PostPage(cls.driver, cls.base_url)
        cls.postPage.open_page()

    def setUp(self):
        self.postPage.click_article()
        self.postPage.click_write()

    def tearDown(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 发布用例1：填写正确标题和正确内容可以发布文章
    def test_post1_correct(self):
        self.postPage.input_title(self.data[1][0])
        self.postPage.input_article(self.data[1][1])
        self.postPage.click_btn()
        self.postPage.click_article()
        actu_text = self.postPage.actual_text()
        self.assertEqual(self.data[1][2], actu_text)

    # 发布用例2：填写正确标题，内容为空可以发布文章
    def test_post2_notl(self):
        self.postPage.input_title(self.data[2][0])
        self.postPage.input_article(self.data[2][1])
        self.postPage.click_btn()
        self.postPage.click_article()
        actu_text = self.postPage.actual_text()
        self.assertIn(self.data[2][2], actu_text)

    # 发布用例3：填写正确内容，标题为空可以发布文章
    def test_post3_noat(self):
        self.postPage.input_title(self.data[3][0])
        self.postPage.input_article(self.data[3][1])
        self.postPage.click_btn()
        self.postPage.click_article()
        actu_text = self.postPage.actual_text()
        self.assertIn(self.data[3][2], actu_text)



