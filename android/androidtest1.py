from time import sleep

import unittest
from androidparent import *


class AndroidTestApiDemos(AndroidParentTest):
    def changeDesiredCaps(self):
        self.desired_caps['appPackage'] = 'io.appium.android.apis'
        self.desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

    def test_find_elements(self):
        el = self.driver.find_element_by_accessibility_id('Graphics')
        el.click()
        el = self.driver.find_element_by_accessibility_id('Arcs')
        self.assertIsNotNone(el)

        self.driver.back()

        el = self.driver.find_element_by_accessibility_id("App")
        self.assertIsNotNone(el)

        els = self.driver.find_elements_by_android_uiautomator("new UiSelector().clickable(true)")
        self.assertGreaterEqual(12, len(els))

        self.driver.find_element_by_android_uiautomator('text("API Demos")')
        self.writeTimer("AndroidTestApiDemos.test_find_elements")
    
    def test_simple_actions(self):
        el = self.driver.find_element_by_accessibility_id('Graphics')
        el.click()

        el = self.driver.find_element_by_accessibility_id('Arcs')
        el.click()

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Graphics/Arcs")')
        self.writeTimer("AndroidTestApiDemos.test_simple_actions")



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTestApiDemos)
    unittest.TextTestRunner(verbosity=2).run(suite)