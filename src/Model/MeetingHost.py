# -*- coding: utf-8 -*-

import datetime
import sqlite3
from sqlite3 import Error

from Constants.TableNames import TableNames
from Constants.Members import Members
from .DBConnection import DBConnection


class MeetingHost():
    def __init__(self):
        self.connection = DBConnection(TableNames().DB_FILE).create()


    def rotateCEOs(self):
        sql = '''
            UPDATE
                users
            SET
                yesterdays_host = ?
            WHERE
                user_number = ?
        '''
        cur = self.connection.cursor()
        currentCEO = self.whichYesterdaysHost(Members().CEOS)
        if currentCEO is Members().NOUTOMI:
            updateParams = [(None, currentCEO), (Members().CEOS, Members().HAMASAKI)]

        elif currentCEO is Members().HAMASAKI:
            updateParams = [(None, currentCEO), (Members().CEOS, Members().NOUTOMI)]

        else:
            print('NO ONE')
            return 

        for updateParam in updateParams:
            cur.execute(sql, updateParam)
        self.connection.commit()


    def rotateEmployees(self):
        sql = '''
            UPDATE
                users
            SET
                yesterdays_host = ?
            WHERE
                user_number = ?
        '''
        cur = self.connection.cursor()
        currentEmployee = self.whichYesterdaysHost(Members().EMPLOYEE)
        if currentEmployee is Members().NO_ONE:
            print('NO ONE')
            return

        nextEmployee = self.getNextEmployee(currentEmployee)
        updateParams = [(None, currentEmployee), (Members().EMPLOYEE, nextEmployee)]
        for updateParam in updateParams:
            cur.execute(sql, updateParam)
        self.connection.commit()


    def fetchoneUserNumber(self, cursor):
        userNumber = cursor.fetchone()
        if userNumber is None:
            return Members().NO_ONE

        return userNumber[0]


    def whichYesterdaysHost(self, hostType):
        sql = '''
            SELECT
                user_number
            FROM
                users
            WHERE
                yesterdays_host = ?
        '''
        cur = self.connection.cursor()
        cur.execute(sql, (hostType, ))

        return self.fetchoneUserNumber(cur)


    def getNextEmployee(self, currentUserNumber):
        sql = '''
            SELECT
                user_number
            FROM
                users
            WHERE
                user_number > ?
            LIMIT 1
        '''
        cur = self.connection.cursor()
        cur.execute(sql, (currentUserNumber, ))

        return self.fetchoneUserNumber(cur)