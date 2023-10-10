__author__ = 'Deepak Manktala'

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CAL.Src.PageObject.Locators import Locator


class AdminLogin(object):

    def __init__(self, driver):
        self.driver = driver

#defining the post registration page object here
        self.adminlink              = driver.find_element(By.XPATH, Locator.adminlink)
        self.adminpageheading       = driver.find_element(By.XPATH, Locator.adminpageheading)
        self.usertest1              = driver.find_element(By.XPATH, Locator.usertest1  )
        self.usertest2              = driver.find_element(By.XPATH, Locator.usertest2   )
        self.Notassigned            = driver.find_element(By.XPATH, Locator.Notassigned )
        self.boardmanagertest1      = driver.find_element(By.XPATH, Locator.boardmanagertest1 )
        self.projectmanagertest1    = driver.find_element(By.XPATH,Locator.projectmanagertest1)
        self.savebuttontest1        = driver.find_element(By.XPATH, Locator.savebuttontest1)
        # self.invalid_login          = driver.find_element(By.XPATH, Locator.invalid_login)
        self.registerlink           = driver.find_element(By.XPATH, Locator.registerlink)
        self.roledropdown           = driver.find_element(By.XPATH, Locator.roledropdown)
    #def getinvalidlogin(self):
    #   return self.invalid_login

    def get_roledropdown(self):
        return self.roledropdown

    def get_adminlink(self):
        return self.adminlink

    def get_adminpage(self):
        return self.adminpageheading

    def get_usertest(self):
        return self.usertest1
    #
    # def getcheckbox(self):
    #     return self.rememberme_checkbox
    #
    # def getsignin(self):
    #     return self.signin
    # def getlogin_heading(self):
    #     return self.login_heading
    #
    # def getforgotpassword(self):
    #     return self.forgot_password