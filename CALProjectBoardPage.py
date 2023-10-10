__author__ = 'Deepak Manktala'

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CAL.Src.PageObject.Locators import Locator


class ProjectBoard(object):

    def __init__(self, driver):
        self.driver = driver

#defining the post registration page object here
        self.omni_logo              = driver.find_element(By.XPATH, Locator.omni_logo)
        self.copyright_label        = driver.find_element(By.XPATH, Locator.copyright_label)
        self.project_status_heading = driver.find_element(By.XPATH, Locator.project_status_heading  )
        self.project_status_link    = driver.find_element(By.XPATH, Locator.project_status_link   )
        self.board_status_link      = driver.find_element(By.XPATH, Locator.board_status_link )
        self.hello_user             = driver.find_element( By.XPATH, Locator.hello_user )
        self.change_password        = driver.find_element( By.XPATH, Locator.change_password )
        self.sign_out               = driver.find_element( By.XPATH, Locator.sign_out )
        self.project_key2           = driver.find_element( By.XPATH, Locator.project_key2 )
        self.project_key1           = driver.find_element( By.XPATH, Locator.project_key1 )

    def getprojectkey1(self):
        return self.project_key1

    def getprojectkey2(self):
        return self.project_key2

    def getprojectstatuslink(self):
        return self.project_status_link
    def getsignout(self):
        return self.sign_out