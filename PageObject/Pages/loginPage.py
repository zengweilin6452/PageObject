# -*- coding: utf-8 -*-

from Pages.basePage import BasePage


class LoginPage(BasePage):
    username_loc = "xpath=//*[@id='user_login']"
    passwd_loc = 'id=user_pass'
    submit_loc = 'id=wp-submit'
    error_loc = 'id=login_error'
    correct_loc = "xpath=.//*[@id='wp-admin-bar-my-account']/a"

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def input_username(self, username_text):
        self.type_value(self.username_loc, username_text)

    def input_passwd(self, passwd_text):
        self.type_value(self.passwd_loc, passwd_text)

    def click_btn(self):
        self.find(self.submit_loc).click()

    def login(self, username, password):
        self.open_url()
        self.input_username(username)
        self.input_passwd(password)
        self.click_btn()

    def actual_text(self, loc):
        return self.find(loc).text
