import os

srcDirPath = os.path.abspath(".")

def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class Paths(object):
    @constant
    def CHROMEDRIVER_EXE():
        return os.path.join(srcDirPath, 'chromedriver.exe')
