#  -*- coding:utf-8 -*-
from Pages.basePage import BasePage
from Pages.loginPage import LoginPage


class PostPage(BasePage):
    title_loc = "id=title"
    text_loc_js_id = "content_ifr"
    publish_loc = "id=publish"
    article_loc = "xpath=.//*[@id='menu-posts']/a/div[3]"
    article_title_loc = "xpath=.//*[@id='the-list']/tr[1]/td[1]/strong"
    write_article_loc = "xpath=.//*[@id='menu-posts']/ul/li[3]/a"
    username = "admin"
    password = "123456"

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def open_page(self):
        LoginPage(self.driver, self.base_url).login(self.username, self.password)

    def input_title(self, title_text):
        self.type_value(self.title_loc, title_text)

    def input_article(self, article_text):
        js_code = "document.getElementById('%s').contentWindow.document.body.innerText='%s';" % (self.text_loc_js_id, article_text)
        self.js(js_code)

    def click_btn(self):
        self.find(self.publish_loc).click()

    def click_article(self):
        self.find(self.article_loc).click()

    def click_write(self):
        self.find(self.write_article_loc).click()

    def actual_text(self):
        return self.find(self.article_title_loc).text



