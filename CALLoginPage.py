__author__ = 'Deepak Manktala'

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CAL.Src.PageObject.Locators import Locator


class Login(object):

    def __init__(self, driver):
        self.driver = driver

#defining the post registration page object here
        self.omni_logo              = driver.find_element(By.XPATH, Locator.omni_logo)
        self.copyright_label        = driver.find_element(By.XPATH, Locator.copyright_label)
        self.username               = driver.find_element(By.XPATH, Locator.username  )
        self.rememberme_checkbox    = driver.find_element(By.XPATH, Locator.rememberme_checkbox   )
        self.sign_in                = driver.find_element(By.XPATH, Locator.sign_in)
        self.login_heading          = driver.find_element(By.XPATH, Locator.login_heading )
        self.forgot_password        = driver.find_element(By.XPATH,Locator.forgot_password)
        self.password               = driver.find_element(By.XPATH, Locator.password)
        #self.invalid_login          = driver.find_element(By.XPATH, Locator.invalid_login)

    #def getinvalidlogin(self):
    #   return self.invalid_login

    def getlogo(self):
        return self.omni_logo

    def getcopyrightlabel(self):
        return self.copyright_label

    def getusername(self):
        return self.username

    def getcheckbox(self):
        return self.rememberme_checkbox

    def getsignin(self):
        return self.sign_in
    def getlogin_heading(self):
        return self.login_heading

    def getforgotpassword(self):
        return self.forgot_password