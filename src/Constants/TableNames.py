import os

srcDirPath = os.path.abspath(".")

def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class TableNames(object):
    @constant
    def DB_FILE():
        modelPath = os.path.join(srcDirPath, 'Model')
        return = os.path.join(modelPath, 'morning_memo_support.db')

    @constant
    def SEEDS():
        return = [
            """ CREATE TABLE IF NOT EXISTS hosts_of_meeting (
                id integer PRIMARY KEY,
                user_number integer NOT NULL,
                yesterdays_host integer,
                monday_host integer
            ); """,
            """ CREATE TABLE IF NOT EXISTS users (
                id integer PRIMARY KEY,
                user_number integer NOT NULL,
                english_name text NOT NULL,
                japanese_name text NOT NULL
            ); """
        ]