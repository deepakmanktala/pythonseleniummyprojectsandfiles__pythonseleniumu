__author__ = 'Deepak Manktala'

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CAL.Src.PageObject.Locators import Locator


class ChangePasswordConfirm(object):

    def __init__(self, driver):
        self.driver = driver

#defining the post registration page object here
        self.omni_logo              = driver.find_element(By.XPATH, Locator.omni_logo)
        self.chngpwdoldpwd          = driver.find_element(By.XPATH, Locator.changepwdoldpwd)
        self.chngpwdnewpwd          = driver.find_element(By.XPATH, Locator.changepwdnewpwd)
        self.chngpwdconfirmpwd      = driver.find_element(By.XPATH, Locator.changepwdconfirmpwd)
        self.changepwdbutton        = driver.find_element(By.XPATH, Locator.changepwdbutton)
        self.hello_user             = driver.find_element( By.XPATH, Locator.hello_user )

    # BoardStatus page Locators
    #def getinvalidlogin(self):
    #   return self.invalid_login

    def getlogo(self):
        return self.omni_logo
  #
  #   def getusername(self):
  #       return self.username
  #
  #   def getcheckbox(self):
  #       return self.rememberme_checkbox
  #
  #   def getsignin(self):
  #       return self.sign_in
  #
  #   def getlogin_heading(self):
  #       return self.login_heading
  #
  #