# coding: utf-8

import re
import os
import datetime
import clipboard

from Constants.Paths import Paths
from Constants.Privates import Privates

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Aipo():
    def __init__(self, chromeDriver):
        self.chromeDriver = chromeDriver
        self.dayNames = ['月', '火', '水', '木', '金', '土', '日']
        self.todayName = self.dayNames[datetime.datetime.today().weekday()]

    def start(self, aipoID, aipoPassword):
        self.loginAipo(aipoID, aipoPassword)

        # select 全員 from select box
        self.chromeDriver.find_element_by_xpath('//div[@class="auiForm"]//select//option[text()="全員"]').click()
        
        noutomidayTds = self.getUserDayTds(self.getTodayTrIndex(23))
        hamasakidayTds = self.getUserDayTds(self.getTodayTrIndex(24))

        scheduleResultStr = '皆様\n\nおはようございます。ジホです。\n'
        scheduleResultStr += '朝ミーティングメモ{monthAndDay}({todayName})です。\n\n\n'.format(monthAndDay=datetime.datetime.now().strftime('%m/%d'), todayName=self.todayName)
        scheduleResultStr += '■ 司会\n今日の司会は岡㟢さんです。\n次回の司会は新川さんです。\n\n\n'

        scheduleResultStr += '■ 遅刻欠席\n'
        scheduleResultStr += '\n\n'

        scheduleResultStr += '■ 今日の一言\n\n\n'

        if '月' == self.todayName:
            schedulePartStr = '■ 今週のスケジュール\n'
            schedulePartStr += '納富 貞嘉\n'
            schedulePartStr += self.getWeekTasks(noutomidayTds)
            schedulePartStr += '浜崎 陽一郎\n'
            schedulePartStr += self.getWeekTasks(hamasakidayTds)
            schedulePartStr += '\n'
        else:
            schedulePartStr = '■ 今日のスケジュール\n'
            schedulePartStr += '納富 貞嘉\n'
            schedulePartStr += self.getTodayTasks(noutomidayTds[0].find_elements_by_tag_name('a')) + '\n'
            schedulePartStr += '浜崎 陽一郎\n'
            schedulePartStr += self.getTodayTasks(hamasakidayTds[0].find_elements_by_tag_name('a'))
            schedulePartStr += '\n\n'
        scheduleResultStr += schedulePartStr
        scheduleResultStr += '■ 連絡事項\n\n\n'
        scheduleResultStr += '以上です。\n今日も一日よろしくお願いします。\n'

        clipboard.copy(scheduleResultStr)
        
        self.chromeDriver.close()

        return scheduleResultStr


    '''
        @param str AIPOのID
        @param str AIPOのPASSWORD
    '''
    def loginAipo(self, aipoID, aipoPassword):
        self.chromeDriver.get(Privates().AIPO_LOGIN_URL)

        self.chromeDriver.find_element_by_name('member_username').send_keys(aipoID)
        self.chromeDriver.find_element_by_name('password').send_keys(aipoPassword)
        self.chromeDriver.find_element_by_name('login_submit').click()

    '''
        AIPOユーザーの当日のスケジュールを持っているtrのindex。

        @param int userID AIPOに見られるユーザーの番号
        @return int userTodayTrIndex 
    '''
    def getTodayTrIndex(self, userID):
        userSearchRule = re.compile(r'aipo\.message\.popupProfile\(' + str(userID) + r',arguments\[0\]\)')
        
        i = 1
        searchMore = True
        while searchMore:
            try:
                xpath = '//*[@id="content-P-16261a88605-1002b"]/div[2]/table/tbody/tr['+ str(i) +']'
                element_present = EC.presence_of_element_located((By.XPATH, xpath))
                tr = WebDriverWait(self.chromeDriver, 3).until(element_present)
                currentTrStr = tr.get_attribute('outerHTML')
                
                if userSearchRule.search(currentTrStr):
                    trsCount = tr.find_element_by_css_selector('th').get_attribute('outerHTML').split('rowspan="')[1].split('"')[0]
                    userTodayTrIndex = i + int(trsCount) - 1
                    return userTodayTrIndex
                i += 1
            except TimeoutException:
                searchMore = False
                print('no element')

    '''
        最初のAIPOの終日タスクが入っているtrタッグのindexを返す。
        
        @param int userID AIPOに見られるユーザーの番号
        @return int userLongTermTrIndex 
    '''
    def getLongTermTrIndex(self, userID):
        trs = self.chromeDriver.find_element_by_xpath('//div[@class="calendarWrapper calendarDisplayWeek"]//tbody').find_elements_by_tag_name('tr')

        userSearchRule = re.compile(r'aipo\.message\.popupProfile\(' + str(userID) + r',arguments\[0\]\)')
        i = 0
        for tr in trs:
            currentTrStr = tr.get_attribute('outerHTML')
            if userSearchRule.search(currentTrStr):
                userLongTermTrIndex = i
            i += 1
            
        return userLongTermTrIndex
    
    '''
        @param int userTodayTrIndex HTML tdタッグを持っているtrタッグのindex。
        @param <List>WebElement trs HTML trタッグになっている。
        @return <List>WebElement userDayTds HTML tdタッグになっている。
    '''
    def getUserDayTds(self, userTodayTrIndex):
        try:
            xpath = '//*[@id="content-P-16261a88605-1002b"]/div[2]/table/tbody/tr['+ str(userTodayTrIndex) +']'
            element_present = EC.presence_of_element_located((By.XPATH, xpath))
            tr = WebDriverWait(self.chromeDriver, 5).until(element_present)
            userDayTds = tr.find_elements_by_tag_name('td')
            return userDayTds
            
        except TimeoutException:
            print('no userDayTds')


    '''
        @param <List>WebElement todayTasks HTML aタッグになっている。
        @return str AIPO上に見えるタスクの集まり
    '''
    def getTodayTasks(self, todayTasks):
        taskResultStr = ''
        for task in todayTasks:
            timeStr = task.find_element_by_css_selector('span.time').get_attribute('innerHTML') + ' '
            taskDetail = task.find_element_by_css_selector('span.title').get_attribute('innerHTML').replace('<wbr>', '')
            taskResultStr += timeStr + taskDetail + '\n'

        return taskResultStr

    '''
        @param <List>WebElement dayTds HTML tdタッグになっている。
        @return str taskResultStr 月曜日から金曜日までのスケジュールを保つ
    '''
    def getWeekTasks(self, dayTds):
        taskResultStr = ''
        weekDayNames = ['金','木','水','火','月']
        copiedDayTds = dayTds[:]
        copiedDayTds.pop()
        copiedDayTds.pop()

        for dayTd in copiedDayTds:
            taskResultStr += weekDayNames.pop() + '\n'
            taskResultStr += self.getTodayTasks(dayTd.find_elements_by_tag_name('a')) + '\n'
            
        return taskResultStr
