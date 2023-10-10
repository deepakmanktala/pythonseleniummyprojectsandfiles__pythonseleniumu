__author__ = 'Deepak Manktala'

import unittest
import datetime
from selenium import webdriver

class EnvironmentSetup(unittest.TestCase):

#setUP contains the browser setup attributes
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\owner\\AppData\\Local\\Programs\\Python\\Python36-32\\chromedriver.exe")
        print ("Run Started at :"+str(datetime.datetime.now()))
        print("Chrome Environment Set Up")
        print("------------------------------------------------------------------")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait( 30 )
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get( "https://cal.omniintegrate.com/omnisolutions" )
        self.driver.implicitly_wait( 30 )

#tearDown method just to close all the browser instances and then quit
    def tearDown(self):
     if (self.driver!=None):
        print("------------------------------------------------------------------")
        print("Test Environment Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))
        self.driver.close()
        self.driver.quit()