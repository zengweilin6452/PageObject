# -*- coding: utf-8 -*-
# _author_ : "zengweilin"

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys


class BasePage(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open_url(self):
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(5)
        assert u'登录' in self.driver.title

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def find(self, loc):
        way = loc.split('=')[0]
        if way.upper() == 'ID':
            value = loc.split('=')[1]
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, value)))

        if way.upper() == 'XPATH':
            val = loc.split('=')[1:]
            value = '='.join(val)
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, value)))

        if way.upper() == 'CSS':
            val = loc.split('=')[1:]
            value = ''.join(val)
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))

        if way.upper() == 'NAME':
            value = loc.split('=')[1]
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, value)))

    def in_frame(self, frame_id):
        return self.driver.switch_to.frame(frame_id)

    def default_frame(self):
        return self.driver.switch_to.default_content()

    def js(self, js_code):
        return self.driver.execute_script(js_code)

    def type_value(self, loc, keys):
        self.find(loc).clear()
        self.find(loc).send_keys(keys)

    def refresh(self):
        self.driver.refresh()

    def get_step_name(self):
        step_name = sys._getframe().f_code.co_name
        return step_name

    def save_screen(self, step):
        time_str = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
        self.driver.save_screenshot(r"../Screenshot/%s%s.png"%(time_str, step))