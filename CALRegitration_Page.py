__author__ = 'Deepak Manktala'

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CAL.Src.PageObject.Locators import Locator


class Registeration( object ):

    def __init__(self, driver):
        self.driver = driver

        # defining the post registration page object here

        #self.registerlink = driver.find_element( By.XPATH, Locator.registerlink )
        self.registerheading = driver.find_element( By.XPATH, Locator.registerheading )
        self.registeremail = driver.find_element( By.XPATH, Locator.registeremail )
        self.registerusername = driver.find_element( By.XPATH, Locator.registerusername )
        self.registerconfirmpwd = driver.find_element( By.XPATH, Locator.registerconfirmpwd )
        self.registerpassword = driver.find_element( By.XPATH, Locator.registerpassword )
        self.registersubmitbutton = driver.find_element( By.XPATH, Locator.registersubmitbutton )
        self.registercancel = driver.find_element( By.XPATH, Locator.registercancel )
        # self.invalid_login          = driver.find_element(By.XPATH, Locator.invalid_login)

    # def getinvalidlogin(self):
    #   return self.invalid_login

    # def get_roledropdown(self):
    #     return self.roledropdown
    #
    # def get_adminlink(self):
    #     return self.adminlink
    #
    # def get_adminpage(self):
    #     return self.adminpageheading
    #
    # def get_usertest(self):
    #     return self.usertest1