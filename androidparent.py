import time

import unittest

from appium import webdriver



class AndroidParentTest(unittest.TestCase):
    def setDesiredCaps(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '8.0.0'
        self.desired_caps['deviceName'] = 'Android Emulator'
        #self.desired_caps['udid'] = '2XJDU17A11000481'
        self.desired_caps['appPackage'] = 'io.appium.android.apis'
        self.desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'
        self.timer = 0
        self.timerstate = 0 # 0 = niet begonnen, 1 = bezig, 2 = gestopt
        self.filename = "androidteststimings.txt"
        self.changeDesiredCaps()
    
    def changeDesiredCaps(self):
        pass

    def setUp(self):
        self.setDesiredCaps()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.startTimer()

    def tearDown(self):
        # end the session
        self.driver.quit()
    
    def startTimer(self):
        self.timer = time.time()
        self.timerstate = 1
    
    def stopTimer(self):
        if self.timerstate == 1:
            self.timer = time.time() - self.timer
            self.timerstate = 2
    
    def writeTimer(self, functionname):
        if self.timerstate != 2:
            self.stopTimer()
        towrite = str((functionname, self.timer))+'\n'
        print(towrite)
        with open(self.filename, "a+") as file:
            file.write(towrite)
    

