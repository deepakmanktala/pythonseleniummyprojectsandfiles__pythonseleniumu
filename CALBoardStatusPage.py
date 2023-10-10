__author__ = 'Deepak Manktala'

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CAL.Src.PageObject.Locators import Locator


class BoardStatus(object):

    def __init__(self, driver):
        self.driver = driver

#defining the post registration page object here
        self.board_status_link      = driver.find_element(By.XPATH, Locator.board_status_link)
        self.board_status_heading   = driver.find_element(By.XPATH, Locator.board_status_heading)
        self.demo_board1            = driver.find_element(By.XPATH, Locator.demo_board1  )
        self.demo_board2            = driver.find_element(By.XPATH, Locator.demo_board2   )
        self.board_type_dropdown    = driver.find_element(By.XPATH, Locator.board_type_dropdown )
        self.test_case_Visa         = driver.find_element(By.XPATH,"//b[(text()='Visa')]")
        self.test_case_MC           = driver.find_element( By.XPATH, "//b[(text()='MasterCard')]" )
        self.test_case_Amex         = driver.find_element( By.XPATH, "//b[(text()='AmericanExpress')]" )
        self.test_case_Discover     = driver.find_element( By.XPATH, "//b[(text()='Discover')]" )
        self.test_case_VisaPayWave  = driver.find_element( By.XPATH, "//b[(text()='VisaPayWave')]" )

    def getboardstatusheading(self):
        return self.board_status_heading

    def getboarddropdown(self):
        return self.board_type_dropdown

    def getboardstatuslink(self):
        return self.board_status_link

    def getdemoboard1(self):
        return self.demo_board1

    def getdemoboard2(self):
        return self.demo_board2
