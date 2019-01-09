# coding: utf-8

import re
import os
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Constants.Paths import Paths
from Constants.Privates import Privates

class HeadlessJob():
    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument("--no-gpu")
        self.driver = webdriver.Chrome(executable_path= Paths().CHROMEDRIVER_EXE, chrome_options=chrome_options)
        self.dayNames = ['月', '火', '水', '木', '金', '土', '日']
        self.todayName = self.dayNames[datetime.datetime.today().weekday()]

    def start(self, tamelID, tamelPassword):
        return self.loginTamel(tamelID, tamelPassword)
        

        self.driver.close()

    '''
        AIPOにログインする。

        @param str AIPOのID
        @param str AIPOのPASSWORD
    '''
    def loginTamel(self, tamelID, tamelPassword):
        self.driver.get(Privates().AIPO_LOGIN_URL)

        self.driver.find_element_by_name('member_username').send_keys(tamelID)
        self.driver.find_element_by_name('password').send_keys(tamelPassword)
        self.driver.find_element_by_name('login_submit').click()

        return 'yes'

        # self.driver.get(Privates().TAMEL_LOGIN_URL)
        # self.driver.find_element_by_name('loginid').send_keys(tamelID)
        # self.driver.find_element_by_name('password').send_keys(tamelPassword)
        # self.driver.find_element_by_xpath("//button[@type='submit']").click()

        # return self.driver.find_element_by_id('tag-cloud').click().get_attribute('outerHTML')

# id tag-cloud