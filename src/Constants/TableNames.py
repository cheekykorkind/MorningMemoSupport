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
        return os.path.join(srcDirPath, 'morning_memo_support.db')

    @constant
    def USERS():
        return """ CREATE TABLE IF NOT EXISTS users (
                    id integer PRIMARY KEY,
                    user_number integer NOT NULL,
                    english_name text NOT NULL,
                    japanese_name text NOT NULL,
                    yesterdays_host integer
                ); """
        