# coding: utf-8

import re
import os
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Constants.Paths import Paths
from Constants.Privates import Privates

class Webdriver():
    def __init__(self):
        self.chrome_options = Options()
        # self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument("--no-gpu")
        self.driver = webdriver.Chrome(executable_path= Paths().CHROMEDRIVER_EXE, chrome_options=self.chrome_options)

    def chromeDriver(self):
        return self.driver