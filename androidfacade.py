from android.androidtest1 import *
import unittest

class AndroidFacade:
    def __init__(self):
        self.suite = unittest.TestSuite()
    
    def addTestClass(self, clz):
        self.suite.addTests(unittest.TestLoader().loadTestsFromTestCase(clz))
    
    def runAllTests(self):
        if self.suite is not None:
            result = unittest.TextTestRunner(verbosity=2).run(self.suite)
            print(result.errors)
            print(result.failures)
    
if __name__ == '__main__':
    facade = AndroidFacade()
    facade.addTestClass(AndroidTestApiDemos)
    facade.runAllTests()
