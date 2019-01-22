# -*- coding: utf-8 -*-

import datetime
import sqlite3
from sqlite3 import Error

from Constants.TableNames import TableNames
from Constants.Members import Members
from . import DBConnection


class MeetingHost():
    def __init__(self):
        self.connection = DBConnection(TableNames().DB_FILE).create()

    def rotateCEOs(self, ceo):
        sql = ''' UPDATE
                    users
                SET
                    yesterdays_host = ?
                WHERE
                    user_number = ?
                AND
                    yesterdays_host = ?
            '''
        cur = self.connection.cursor()
        cur.execute(sql, task)