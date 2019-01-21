# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error
from Constants.TableNames import TableNames


def createConnection(dbFile):
    try:
        return sqlite3.connect(dbFile)
    except Error as e:
        print(e)

def createTable(conn, create_table_sql):
    try:
        conn.cursor().execute(create_table_sql)
    except Error as e:
        print(e)

    return None

def createUsers(conn, user):
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
            VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    return cur.lastrowid

            # create a new project
            # project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
        

if __name__ == "__main__":
    # dbFile = "morning_memo_support.db"
    tables = TableNames().SEEDS
    
    # connection = createConnection(TableNames().DB_FILE)
    print(connection)
    if connection is not None:
        for table in tables:
            createTable(connection, table)
    else:
        print("Error! cannot create the database connection.")

