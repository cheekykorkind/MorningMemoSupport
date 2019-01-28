# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error


class DBConnection():
    def __init__(self, dbFile):
        try:
            self.connetion = sqlite3.connect(dbFile)
        except Error as e:
            print(e)
            self.connetion = None
    
    def create(self):
        return self.connetion

