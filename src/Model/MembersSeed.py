# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error
 
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Constants.TableNames import TableNames
from Constants.Members import Members
from DBConnection import DBConnection


def createTable(conn, create_table_sql):
    try:
        conn.cursor().execute(create_table_sql)
    except Error as e:
        print(e)

    return None


def insertUsers(conn, user):
    sql = ''' INSERT INTO users(user_number,english_name,japanese_name)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)

    return cur.lastrowid


if __name__ == "__main__":
    connection = DBConnection(TableNames().DB_FILE).create()
    if connection is not None:
        createTable(connection, TableNames().USERS)
        for member in Members().LIST:
            insertUsers(connection, member)
        connection.commit()
        
    else:
        print("Error! cannot create the database connection.")

