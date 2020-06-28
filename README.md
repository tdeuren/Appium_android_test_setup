# Appium_android_test_setup
This is a simple setup for android app testing using appium. The facade pattern is used. 

If you want to add more tests, you should write a testcase using AndroidParentTest as the parent class and store the file in the folder android. If you want to use it, simply call addTestClass on the facade with as parameter the name of the class. The function runAllTests on the facade runs all the tests added with function addTestClass.
