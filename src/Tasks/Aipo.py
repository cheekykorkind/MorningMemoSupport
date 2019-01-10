# coding: utf-8

import re
import os
import datetime

from Constants.Paths import Paths
from Constants.Privates import Privates

class Aipo():
    def __init__(self, chromeDriver):
        self.chromeDriver = chromeDriver
        self.dayNames = ['月', '火', '水', '木', '金', '土', '日']
        self.todayName = self.dayNames[datetime.datetime.today().weekday()]

    def start(self, aipoID, aipoPassword):
        return self.loginAipo(aipoID, aipoPassword)
        
        self.chromeDriver.close()

    '''
        AIPOにログインする。

        @param str AIPOのID
        @param str AIPOのPASSWORD
    '''
    def loginAipo(self, aipoID, aipoPassword):
        self.chromeDriver.get(Privates().AIPO_LOGIN_URL)

        self.chromeDriver.find_element_by_name('member_username').send_keys(aipoID)
        self.chromeDriver.find_element_by_name('password').send_keys(aipoPassword)
        self.chromeDriver.find_element_by_name('login_submit').click()

        return 'yes'