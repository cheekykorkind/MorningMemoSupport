# coding: utf-8

from Constants.Paths import Paths
# from Constants.Privates import Privates
from Constants.Members import Members
from Model.MeetingHost import MeetingHost

import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Tamel():
    def __init__(self, chromeDriver):
        self.chromeDriver = chromeDriver

    def start(self, tamelID, tamelPassword):
        self.loginTamel(tamelID, tamelPassword)

        self.chromeDriver.get(Privates().TAMEL_MEETING_HOSTS_URL)
        meetingHostsList = self.chromeDriver.find_elements_by_xpath('//*[@id="article-main"]/ol/li')

        result = ''
        for meetingHost in meetingHostsList:
            result += meetingHost.get_attribute('innerHTML') + '\n'
                    
        # self.chromeDriver.close()

        return result

    def updateTest(self):
        if self.isFirstOfweekdays():
            MeetingHost().rotateCEOs()
            return

        MeetingHost().rotateEmployees()


    '''
        @param str TamelのID
        @param str TamelのPASSWORD
    '''
    def loginTamel(self, tamelID, tamelPassword):
        self.chromeDriver.get(Privates().TAMEL_LOGIN_STEP1_URL)
        self.chromeDriver.find_element_by_xpath('//*[@id="fsso-login"]').click()

        try:
            self.chromeDriver.switch_to_window(self.chromeDriver.window_handles[1])

            xpath = '//*[@id="loginid"]'
            idParent = EC.presence_of_element_located((By.XPATH, xpath))
            loginForm = WebDriverWait(self.chromeDriver, 5).until(idParent)
            loginForm.send_keys(tamelID)

            xpath = '//*[@id="password"]'
            passwordPresent = EC.presence_of_element_located((By.XPATH, xpath))
            passwordForm = WebDriverWait(self.chromeDriver, 5).until(passwordPresent)
            passwordForm.send_keys(tamelPassword)

            xpath = '//*[@id="content"]/div/div/form/button'
            loginBtnParent = EC.presence_of_element_located((By.XPATH, xpath))
            loginBtn = WebDriverWait(self.chromeDriver, 5).until(loginBtnParent)
            loginBtn.click()
            self.chromeDriver.switch_to_window(self.chromeDriver.window_handles[0])

        except TimeoutException:
            print('no loginTamel')


    def isFirstOfweekdays(self):
        if datetime.datetime.today().weekday() is 0:
            return True
        
        return False