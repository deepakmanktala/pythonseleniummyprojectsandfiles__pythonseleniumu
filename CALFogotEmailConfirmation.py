__author__ = 'Deepak Manktala'

import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CAL.Src.PageObject.Locators import Locator


class ForgotConfirm(object):

    def __init__(self, driver):
        self.driver = driver

#defining the post registration page object here
        self.omni_logo              = driver.find_element(By.XPATH, Locator.omni_logo)
        self.copyright_label        = driver.find_element(By.XPATH, Locator.copyright_label)
        self.loginlink              = driver.find_element( By.XPATH,Locator.loginlink )